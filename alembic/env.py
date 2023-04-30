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
COPY public.images (film_id, id, image_url) FROM '$$PATH$$/images.dat';

--
-- Name: films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN id SET DEFAULT nextval('public.films_id_seq'::regclass);

--
-- Name: id; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_id_seq OWNER TO postgres;
