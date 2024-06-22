DROP TABLE IF EXISTS document;
DROP TABLE IF EXISTS photo;
DROP TABLE IF EXISTS person;

CREATE TABLE person
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    nationality VARCHAR(32),
    date_of_birth DATE,
    place_of_birth VARCHAR(32),
    personal_id_no VARCHAR(32),
    sex CHAR(1),
    face_data FLOAT[5]
);

CREATE TABLE photo
(
    id SERIAL PRIMARY KEY,
    data FLOAT[5]
);

CREATE TABLE document
(
    id SERIAL PRIMARY KEY,
    person_id INT,
    photo_id INT,
    number VARCHAR(16),
    expiry_date DATE,

    CONSTRAINT FK_person_id FOREIGN KEY (person_id) REFERENCES person(id),
    CONSTRAINT FK_photo_id FOREIGN KEY (photo_id) REFERENCES photo(id)
);

CREATE OR REPLACE FUNCTION update_face_data()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE person
    SET face_data = (
        SELECT array_divide_by_int(data_sum, cnt)
        FROM (
            SELECT array_sum_agg(p.data) AS data_sum, CAST(COUNT(*) AS INT) AS cnt
            FROM document d
            JOIN photo p ON p.id = d.photo_id
            WHERE d.person_id = NEW.person_id
        ) AS p
    )
    WHERE id = NEW.person_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS update_face_data_trigger ON document;

CREATE TRIGGER update_face_data_trigger
AFTER UPDATE OR INSERT OR DELETE ON document
FOR EACH ROW
EXECUTE FUNCTION update_face_data();

CREATE OR REPLACE FUNCTION array_sum(FLOAT[], FLOAT[])
RETURNS FLOAT[] LANGUAGE sql immutable AS $$
    SELECT array_agg(coalesce(a, 0) + b)
    FROM unnest($1, $2) AS u(a, b)
$$;

CREATE OR REPLACE FUNCTION array_dist(face_data1 FLOAT[], face_data2 FLOAT[])
RETURNS FLOAT LANGUAGE sql IMMUTABLE AS $$
    SELECT sqrt(sum((coalesce(a, 0) - coalesce(b, 0))^2))
    FROM unnest(face_data1, face_data2) AS u(a, b)
$$;

CREATE OR REPLACE FUNCTION array_divide_by_int(FLOAT[], INTEGER)
RETURNS FLOAT[] LANGUAGE sql immutable AS $$
    SELECT array_agg(coalesce(a, 0) / $2)
    FROM unnest($1) AS u(a)
$$;

CREATE OR REPLACE FUNCTION find_closest_person(target_vector FLOAT[])
RETURNS TABLE (
    person_id INT,
    distance FLOAT
) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT id, array_dist(p.face_data, target_vector) AS distance
    FROM person p
    ORDER BY distance
    LIMIT 1;
END;
$$;

DROP AGGREGATE IF EXISTS array_sum_agg(FLOAT[]);

CREATE AGGREGATE array_sum_agg(FLOAT[]) (
    SFUNC = array_sum,
    STYPE = FLOAT[]
);

INSERT INTO person VALUES
(DEFAULT, 'Andrzej', 'Abacki', 'PL', '2001-01-16', 'Kraków', '01234567890123', 'm', NULL),
(DEFAULT, 'Bogdan', 'Babacki', 'PL', '2001-05-18', 'Kraków', '25209515986168', 'm', NULL);

INSERT INTO photo VALUES
(DEFAULT, '{0.2, 0.3, 0.8, 1.0, 0.15}'),
(DEFAULT, '{0.5, 0.8, 0.2, 0.8, 0.5}'),
(DEFAULT, '{0.15, 0.35, 0.8, 0.9, 0.25}');

INSERT INTO document VALUES
(DEFAULT, 1, 1, 'ESZ 141777', '2026-03-18'),
(DEFAULT, 2, 2, 'ESZ 123456', '2024-02-05'),
(DEFAULT, 1, 3, 'ESZ 654894', '2026-03-18');

--SELECT * FROM find_closest_person('{0.2, 0.3, 0.8, 1.0, 0.15}'); RESULT (1, 0.0790569415042095)
--SELECT * FROM find_closest_person('{0.5, 0.8, 0.2, 0.8, 0.5}'); RESULT (2, 0)