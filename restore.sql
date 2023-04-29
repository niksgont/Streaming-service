--
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE films;
--
-- Name: films; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE films WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';


ALTER DATABASE films OWNER TO postgres;

\connect films

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    actor_id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255)
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    film_id integer NOT NULL,
    category_name character varying(255) NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: filmcast; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.filmcast (
    film_id integer NOT NULL,
    actor_id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255)
);


ALTER TABLE public.filmcast OWNER TO postgres;

--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    director character varying(255) NOT NULL,
    description character varying(1000) NOT NULL,
    year integer NOT NULL,
    length smallint NOT NULL,
    rating character varying(255) NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: images; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.images (
    film_id integer,
    id integer NOT NULL,
    image_url character varying(500)
);


ALTER TABLE public.images OWNER TO postgres;

--
-- Name: images_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.images_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_id_seq OWNER TO postgres;

--
-- Name: images_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.images_id_seq OWNED BY public.images.id;


--
-- Name: images id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images ALTER COLUMN id SET DEFAULT nextval('public.images_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (actor_id, first_name, last_name) FROM stdin;
\.
COPY public.actor (actor_id, first_name, last_name) FROM '$$PATH$$/3352.dat';

--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (film_id, category_name) FROM stdin;
\.
COPY public.category (film_id, category_name) FROM '$$PATH$$/3351.dat';

--
-- Data for Name: filmcast; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.filmcast (film_id, actor_id, first_name, last_name) FROM stdin;
\.
COPY public.filmcast (film_id, actor_id, first_name, last_name) FROM '$$PATH$$/3353.dat';

--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (id, title, director, description, year, length, rating) FROM stdin;
\.
COPY public.films (id, title, director, description, year, length, rating) FROM '$$PATH$$/3350.dat';

--
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.images (film_id, id, image_url) FROM stdin;
\.
COPY public.images (film_id, id, image_url) FROM '$$PATH$$/3355.dat';

--
-- Name: images_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.images_id_seq', 10, true);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (actor_id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (film_id, category_name);


--
-- Name: filmcast filmcast_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.filmcast
    ADD CONSTRAINT filmcast_pkey PRIMARY KEY (film_id, actor_id);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (id);


--
-- Name: images images_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (id);


--
-- Name: actor_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX actor_id_idx ON public.actor USING btree (actor_id);


--
-- Name: actor_last_name_hash_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX actor_last_name_hash_idx ON public.actor USING hash (last_name);


--
-- Name: category_cat_name_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX category_cat_name_idx ON public.category USING hash (category_name);


--
-- Name: category_film_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX category_film_id_idx ON public.category USING btree (film_id);


--
-- Name: films_director_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX films_director_idx ON public.films USING hash (director);


--
-- Name: films_id_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX films_id_idx ON public.films USING btree (id);


--
-- Name: films_rating_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX films_rating_idx ON public.films USING btree (id, rating);


--
-- Name: films_title_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX films_title_idx ON public.films USING hash (title);


--
-- PostgreSQL database dump complete
--

