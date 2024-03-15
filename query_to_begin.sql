CREATE TABLE cards (
    id bigserial NOT NULL,
    value varchar(120) NOT NULL,
    CONSTRAINT idx_16419_primary PRIMARY KEY (id)
);
CREATE UNIQUE INDEX idx_value ON cards USING btree (value);

CREATE TABLE "user" (
    id bigserial NOT NULL,
    username varchar(120) NOT NULL,
    token varchar(260) NOT NULL,
    CONSTRAINT idx_123123_primary PRIMARY KEY (id)
);


insert into "user" (username, token)
select 
    name,
    token
from
    (select replace(sha256(concat('david.fagundes', ':', '123456')::bytea)::text, '\x', '') as token, 'david.fagundes' as name) as psswd;