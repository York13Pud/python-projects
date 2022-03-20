/* Table for the customer infofmation */


/* Table for the speedtest locations */

CREATE TABLE speed_test_location(
    ID          INT     PRIMARY KEY NOT NULL,
    REF_ID      INT                 NOT NULL,
    HOST        TEXT                NOT NULL,
    PORT        TEXT                NOT NULL,
    NAME        TEXT                NOT NULL,
    LOCATION    TEXT                NOT NULL,
    COUNTRY     TEXT                NOT NULL
)

/* Table for the speedtest results */