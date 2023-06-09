drop table if exists int_clean_data_cleaned cascade;
drop table if exists dom_cleaned_data cascade;
drop table if exists percent_change_post_covid cascade;


CREATE TABLE "int_clean_data_cleaned" (
    "time" date not null,
	"country" varchar not null,
	"commodity" varchar not null,
	"price" float	
);

CREATE TABLE "dom_cleaned_data" (
    "month" date not null,
    "country" varchar NOT NULL,
	"price_type" varchar not null,
	"market" varchar not null,
	"price" float not null
);

CREATE TABLE "percent_change_post_covid" (
	"country" varchar not null,
	"price_type" varchar not null,
	"market" varchar not null,
	"commodity" varchar not null,
	"post_covid" float not null,
	"yearly" float not null
)

--Import csv's manually into each table
select * from int_clean_data_cleaned limit 20
select * from dom_cleaned_data limit 20
select * from percent_change_post_covid limit 20