CREATE TABLE scores (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    score INTEGER,
    region TEXT
);

INSERT INTO scores (score, region) VALUES
    (60, 'EU'),
    (88, 'EU'),
    (75, 'NA'),
    (95, 'NA'),
    (60, 'AS'),
    (75, 'EU'),
    (45, 'NA'),
    (100, 'EU');
-- Do not modify above this line. --
SELECT min(score),max(score),round(avg(score))as min_score max_score avg_score
FROM scores
WHERE region='EU';





