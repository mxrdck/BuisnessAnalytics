--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

-- Started on 2021-01-26 21:37:00

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
-- TOC entry 203 (class 1259 OID 16893)
-- Name: HealthParameter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."HealthParameter" (
    id integer NOT NULL,
    denotation character varying(256) NOT NULL
);


ALTER TABLE public."HealthParameter" OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16891)
-- Name: HealthParameter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."HealthParameter_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."HealthParameter_id_seq" OWNER TO postgres;

--
-- TOC entry 3029 (class 0 OID 0)
-- Dependencies: 202
-- Name: HealthParameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."HealthParameter_id_seq" OWNED BY public."HealthParameter".id;


--
-- TOC entry 205 (class 1259 OID 16903)
-- Name: HealthValue; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."HealthValue" (
    id integer NOT NULL,
    value integer NOT NULL,
    parameter integer
);


ALTER TABLE public."HealthValue" OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16901)
-- Name: HealthValue_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."HealthValue_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."HealthValue_id_seq" OWNER TO postgres;

--
-- TOC entry 3030 (class 0 OID 0)
-- Dependencies: 204
-- Name: HealthValue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."HealthValue_id_seq" OWNED BY public."HealthValue".id;


--
-- TOC entry 201 (class 1259 OID 16882)
-- Name: Patient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Patient" (
    id integer NOT NULL,
    height double precision NOT NULL,
    weight double precision NOT NULL,
    first_name character varying(256) NOT NULL,
    last_name character varying(256) NOT NULL,
    sex character varying NOT NULL
);


ALTER TABLE public."Patient" OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16880)
-- Name: Patient_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Patient_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Patient_id_seq" OWNER TO postgres;

--
-- TOC entry 3031 (class 0 OID 0)
-- Dependencies: 200
-- Name: Patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Patient_id_seq" OWNED BY public."Patient".id;


--
-- TOC entry 207 (class 1259 OID 16916)
-- Name: patient_health; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient_health (
    id integer NOT NULL,
    patient_id integer,
    healthvalue_id integer,
    date date
);


ALTER TABLE public.patient_health OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16914)
-- Name: patient_health_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patient_health_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_health_id_seq OWNER TO postgres;

--
-- TOC entry 3032 (class 0 OID 0)
-- Dependencies: 206
-- Name: patient_health_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patient_health_id_seq OWNED BY public.patient_health.id;


--
-- TOC entry 2870 (class 2604 OID 16896)
-- Name: HealthParameter id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthParameter" ALTER COLUMN id SET DEFAULT nextval('public."HealthParameter_id_seq"'::regclass);


--
-- TOC entry 2871 (class 2604 OID 16906)
-- Name: HealthValue id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthValue" ALTER COLUMN id SET DEFAULT nextval('public."HealthValue_id_seq"'::regclass);


--
-- TOC entry 2869 (class 2604 OID 16885)
-- Name: Patient id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Patient" ALTER COLUMN id SET DEFAULT nextval('public."Patient_id_seq"'::regclass);


--
-- TOC entry 2872 (class 2604 OID 16919)
-- Name: patient_health id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_health ALTER COLUMN id SET DEFAULT nextval('public.patient_health_id_seq'::regclass);


--
-- TOC entry 3019 (class 0 OID 16893)
-- Dependencies: 203
-- Data for Name: HealthParameter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."HealthParameter" (id, denotation) FROM stdin;
3	Eisen
4	Magnesium
5	Puls
7	THC
25	Körperfettanteil
26	Weiße Blutkörperchen
\.


--
-- TOC entry 3021 (class 0 OID 16903)
-- Dependencies: 205
-- Data for Name: HealthValue; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."HealthValue" (id, value, parameter) FROM stdin;
710	513	5
18	84	4
19	41	5
24	62	3
25	56	4
26	95	5
28	43	7
31	10	3
32	74	4
33	62	5
35	36	7
38	81	3
39	84	4
40	17	5
42	19	7
45	0	3
46	30	4
47	71	5
49	80	7
52	83	3
53	4	4
54	43	5
56	62	7
59	7	3
60	95	4
61	85	5
63	36	7
66	56	3
67	28	4
68	61	5
70	100	7
73	17	3
74	60	4
75	64	5
77	56	7
80	34	3
81	50	4
82	77	5
84	11	7
87	99	3
88	39	4
89	35	5
91	25	7
94	45	3
95	77	4
96	51	5
98	76	7
101	21	3
102	41	4
103	88	5
105	57	7
108	58	3
109	9	4
110	2	5
112	19	7
115	92	3
116	50	4
117	11	5
119	86	7
122	10	3
123	74	4
124	68	5
126	64	7
129	2	3
130	38	4
131	10	5
133	38	7
136	95	3
137	51	4
138	37	5
140	92	7
143	63	3
144	81	4
145	6	5
147	51	7
150	3	3
151	28	4
152	25	5
154	34	7
164	72	3
165	22	4
166	89	5
168	36	7
178	55	3
179	70	4
180	30	5
182	33	7
711	99	4
715	33	3
716	45	3
192	10	3
193	69	4
194	17	5
717	9	7
196	7	7
718	10	25
719	15	25
199	29	3
200	25	4
201	50	5
720	33	4
203	77	7
721	1	26
234	91	3
235	16	4
236	44	5
238	94	7
241	66	3
242	51	4
243	1	5
245	32	7
248	73	3
249	72	4
250	46	5
252	92	7
255	66	3
256	22	4
257	75	5
259	76	7
262	64	3
263	54	4
264	10	5
266	39	7
269	94	3
270	57	4
271	1	5
273	65	7
283	40	3
284	50	4
285	18	5
287	14	7
290	33	3
291	63	4
292	40	5
294	12	7
297	68	3
298	47	4
299	62	5
301	70	7
304	86	3
305	38	4
306	91	5
308	77	7
311	30	3
312	28	4
313	70	5
315	7	7
318	97	3
319	55	4
320	74	5
322	59	7
325	43	3
326	98	4
327	48	5
329	30	7
332	66	3
333	69	4
334	77	5
336	88	7
339	48	3
340	51	4
341	55	5
343	56	7
353	39	3
354	76	4
355	42	5
357	88	7
360	66	3
361	45	4
362	30	5
364	56	7
367	30	3
368	88	4
369	98	5
371	20	7
712	99	3
374	37	3
375	71	4
376	42	5
378	51	7
381	18	3
382	5	4
383	27	5
385	8	7
388	33	3
389	20	4
390	26	5
392	82	7
395	32	3
396	42	4
397	20	5
399	57	7
402	90	3
403	66	4
404	60	5
406	85	7
409	26	3
410	17	4
411	10	5
413	15	7
416	73	3
417	18	4
418	68	5
420	53	7
423	5	3
424	16	4
425	83	5
427	15	7
430	24	3
431	99	4
432	64	5
434	36	7
437	85	3
438	42	4
441	37	7
444	97	3
445	21	4
446	39	5
448	61	7
451	4	3
452	0	4
453	80	5
455	83	7
458	94	3
459	13	4
460	95	5
462	60	7
465	18	3
466	57	4
467	45	5
469	68	7
472	2	3
473	21	4
474	35	5
476	95	7
479	53	3
480	98	4
481	7	5
483	98	7
486	72	3
487	7	4
488	38	5
490	39	7
493	71	3
494	17	4
495	38	5
497	80	7
500	88	3
501	34	4
502	99	5
504	10	7
507	5	3
508	50	4
509	71	5
511	41	7
514	93	3
515	29	4
516	49	5
518	84	7
521	77	3
522	97	4
523	91	5
525	75	7
528	38	3
529	86	4
530	14	5
532	35	7
535	74	3
536	94	4
537	56	5
539	68	7
542	88	3
543	68	4
544	0	5
546	81	7
549	16	3
550	42	4
551	18	5
553	61	7
556	91	3
557	86	4
558	7	5
713	17	3
560	39	7
563	25	3
564	17	4
565	39	5
567	42	7
570	99	3
571	74	4
572	66	5
574	87	7
577	81	3
578	41	4
579	65	5
581	91	7
584	82	3
585	9	4
586	7	5
588	92	7
591	67	3
592	12	4
593	3	5
595	75	7
598	22	3
599	73	4
600	72	5
602	44	7
605	81	3
606	82	4
607	14	5
609	99	7
612	31	3
613	8	4
614	29	5
616	91	7
619	71	3
620	71	4
621	47	5
623	90	7
626	66	3
627	69	4
628	11	5
630	87	7
633	24	3
634	66	4
635	19	5
637	13	7
640	81	3
641	70	4
642	19	5
644	11	7
647	86	3
648	9	4
649	83	5
651	8	7
654	40	3
655	78	4
656	54	5
658	64	7
661	46	3
662	40	4
663	57	5
665	8	7
668	95	3
669	87	4
670	50	5
672	49	7
675	30	3
676	51	4
677	35	5
679	92	7
682	3	3
683	71	4
684	88	5
686	91	7
689	98	3
690	88	4
691	75	5
693	45	7
696	56	3
697	58	4
698	74	5
700	85	7
\.


--
-- TOC entry 3017 (class 0 OID 16882)
-- Dependencies: 201
-- Data for Name: Patient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Patient" (id, height, weight, first_name, last_name, sex) FROM stdin;
3	1.62	49.28	Loretta	Israel	female
4	1.68	174.14	Billy	Smith	male
5	1.84	67.89	Loraine	Strickland	female
6	1.79	121.55	Barbara	Mcghee	female
7	1.68	107.65	Gilbert	Salinas	male
8	1.64	63.7	Candelaria	Kaba	female
9	1.52	157.86	Anne	Fields	female
10	1.64	137.51	Nell	Nettles	female
11	1.52	123.34	Tamala	Hottinger	female
12	1.53	146.19	Brenda	Wright	female
13	1.65	64.63	Bernice	Williams	female
14	1.55	131.53	Stephen	Thomas	male
15	1.85	69.63	Emmett	Ostrander	male
16	1.78	155.45	Pat	Boswell	male
17	1.95	145.02	Donald	Wekenborg	male
18	1.88	139.65	Morgan	Hubbard	male
19	1.62	147.15	Denise	Ishikawa	female
20	1.55	77.7	Michael	Webster	male
21	1.78	148.68	Karen	Swilley	female
22	1.66	61	Palmer	Haynes	male
24	1.54	177.03	Tristan	Little	female
26	1.7	56.86	Joe	Musetti	female
28	1.65	63.63	Luis	Einhorn	male
29	1.79	178.31	Kara	Ceballos	female
34	1.91	123.51	Michelle	Oliveira	female
35	1.75	162.87	Steven	Lloyd	male
36	1.69	156.5	Marie	Desai	female
37	1.8	109.05	Charles	Crabtree	male
38	1.67	135.51	Rachel	Arimoto	female
39	1.96	65.38	Sally	Wyatt	female
41	1.71	126.17	Melinda	Bogard	female
42	1.56	113.94	William	Ontiveros	male
43	1.63	144.22	Debra	Higginbotham	female
44	1.87	68.53	Teddy	Anderson	male
45	1.98	113.04	Deidre	Gibbs	female
46	1.54	63.91	Janelle	Donato	female
47	1.83	93.61	Dawn	Reyna	female
48	1.97	41.04	Carolyn	Player	female
49	1.61	144.62	Marcia	Marshall	female
51	1.72	48.22	Holly	Trexler	female
52	1.91	124.02	Javier	Floyd	male
53	1.59	47.5	Emily	Russell	female
54	1.55	84.43	Robert	Stevenson	male
55	1.9	119.94	Willie	Marshal	male
56	1.99	175.46	Danielle	Taylor	female
57	1.55	65.36	Timothy	Yazzie	male
58	1.64	96.23	Sara	Sandridge	female
59	1.65	73.57	Emma	Drake	female
60	1.6	98.45	Deloris	Boshart	female
61	1.71	94.1	Laurie	Felix	female
62	1.84	105.47	Melvin	Hendricks	male
63	1.78	160.25	Amanda	Snyder	female
64	2	93.59	Shannon	Martin	female
65	1.72	92.15	Michael	Bland	male
66	1.53	96.64	Sam	Loomis	male
67	1.66	126.1	Fred	Dorsey	male
68	1.58	54.89	Ralph	Gardiner	male
69	1.54	152.22	William	Nickel	male
70	1.91	141.13	Mary	Handy	female
71	1.88	109.25	Jeffery	Edgell	male
72	1.98	115.57	Lisa	Kauffman	female
73	1.97	63.92	Jill	Hester	female
74	1.68	177.67	Maryann	Roberson	female
75	1.65	172.09	Kelli	Mesa	female
76	1.53	107.18	Paul	Keen	male
77	1.71	80.49	William	Jones	male
78	1.55	56.61	Ethel	Tolson	female
79	1.99	61.8	David	Exler	male
80	1.52	123.74	Gloria	Brown	female
81	1.61	131.33	Carl	Martinez	male
82	1.99	80.12	Brenda	Allison	female
83	1.68	105.53	Lisa	Contreras	female
84	1.8	170.57	Anita	Carter	female
85	1.73	173.25	Robert	Reidy	male
86	1.64	150.87	Sheila	Dennis	female
87	1.54	47.56	Peter	Ranger	male
88	1.99	160.04	Margaret	Hawkins	female
89	1.7	165.45	Bridget	Grimes	female
90	1.61	87.77	Larry	Kuhn	male
91	1.64	172.66	Mary	Bender	female
92	1.6	149.89	Amber	Evans	female
93	1.68	175.98	William	Gupta	male
94	1.92	88.41	Mary	Frank	female
95	1.9	153.11	Joe	Gibson	male
96	1.78	155.44	Catherine	Hulsey	female
97	1.74	164.58	Amy	Smith	female
98	1.74	104.73	Amanda	Pace	female
99	1.86	136	Wilbert	Jones	male
100	1.85	155.23	Dennis	Daley	male
101	1.86	83	Max	Rudeck	male
102	1.88	86	Rüdiger	Rüdicher	male
103	1.88	86	Rüdiger	Rüdicher	male
104	2	99	GUIMensch	GUIMENSCH	männlich
105	1.88	67	aaaaaaaaaa	asdfasdff	männlich
106	1.34	73	Harald	Hardcore	männlich
107	1.34	44	Reinhard	Rausweich	männlich
108	1.75	12	Theo	Frey	männlich
109	44	22	poawqieujrfpaoewijrf	aisodpfj	männlich
110	12	33	asdfasdf	asdfasdf	männlich
111	12	33	Kekling	Hezmin	männlich
113	1.85	44	wohä	hezmin	männlich
114	22	22	asdfasdf	asdfasdf	männlich
116	1.56	67	Al	Hezmin	männlich
118	11	22	Max	RUdeck	männlich
119	11	88	Theo	Frey	weiblich
121	11	11	sdfgsdfg	sdfgsdfg	männlich
122	1.88	99	GUIPatient	Vorführung	männlich
123	1.45	56	asdfasdf	asdfasdf	männlich
124	11	11	asdfasd	asdfasdf	männlich
\.


--
-- TOC entry 3023 (class 0 OID 16916)
-- Dependencies: 207
-- Data for Name: patient_health; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient_health (id, patient_id, healthvalue_id, date) FROM stdin;
705	3	710	2021-01-26
710	122	715	2021-01-12
711	122	716	2021-01-12
712	122	717	2021-01-12
713	122	718	2021-01-12
714	122	719	2021-01-15
715	122	720	2021-01-20
716	3	721	2021-01-01
18	3	18	2020-12-21
19	3	19	2020-12-21
24	4	24	2020-12-21
25	4	25	2020-12-21
26	4	26	2020-12-21
28	4	28	2020-12-21
31	5	31	2020-12-21
32	5	32	2020-12-21
33	5	33	2020-12-21
35	5	35	2020-12-21
38	6	38	2020-12-21
39	6	39	2020-12-21
40	6	40	2020-12-21
42	6	42	2020-12-21
45	7	45	2020-12-21
46	7	46	2020-12-21
47	7	47	2020-12-21
49	7	49	2020-12-21
52	8	52	2020-12-21
53	8	53	2020-12-21
54	8	54	2020-12-21
56	8	56	2020-12-21
59	9	59	2020-12-21
60	9	60	2020-12-21
61	9	61	2020-12-21
63	9	63	2020-12-21
66	10	66	2020-12-21
67	10	67	2020-12-21
68	10	68	2020-12-21
70	10	70	2020-12-21
73	11	73	2020-12-21
74	11	74	2020-12-21
75	11	75	2020-12-21
77	11	77	2020-12-21
80	12	80	2020-12-21
81	12	81	2020-12-21
82	12	82	2020-12-21
84	12	84	2020-12-21
87	13	87	2020-12-21
88	13	88	2020-12-21
89	13	89	2020-12-21
91	13	91	2020-12-21
94	14	94	2020-12-21
95	14	95	2020-12-21
96	14	96	2020-12-21
98	14	98	2020-12-21
101	15	101	2020-12-21
102	15	102	2020-12-21
103	15	103	2020-12-21
105	15	105	2020-12-21
108	16	108	2020-12-21
109	16	109	2020-12-21
110	16	110	2020-12-21
112	16	112	2020-12-21
115	17	115	2020-12-21
116	17	116	2020-12-21
117	17	117	2020-12-21
119	17	119	2020-12-21
122	18	122	2020-12-21
123	18	123	2020-12-21
124	18	124	2020-12-21
126	18	126	2020-12-21
129	19	129	2020-12-21
130	19	130	2020-12-21
131	19	131	2020-12-21
133	19	133	2020-12-21
136	20	136	2020-12-21
137	20	137	2020-12-21
138	20	138	2020-12-21
140	20	140	2020-12-21
143	21	143	2020-12-21
144	21	144	2020-12-21
145	21	145	2020-12-21
147	21	147	2020-12-21
706	38	711	2021-01-26
150	22	150	2020-12-21
151	22	151	2020-12-21
152	22	152	2020-12-21
154	22	154	2020-12-21
164	24	164	2020-12-21
165	24	165	2020-12-21
166	24	166	2020-12-21
168	24	168	2020-12-21
178	26	178	2020-12-21
179	26	179	2020-12-21
180	26	180	2020-12-21
182	26	182	2020-12-21
192	28	192	2020-12-21
193	28	193	2020-12-21
194	28	194	2020-12-21
196	28	196	2020-12-21
199	29	199	2020-12-21
200	29	200	2020-12-21
201	29	201	2020-12-21
203	29	203	2020-12-21
234	34	234	2020-12-21
235	34	235	2020-12-21
236	34	236	2020-12-21
238	34	238	2020-12-21
241	35	241	2020-12-21
242	35	242	2020-12-21
243	35	243	2020-12-21
245	35	245	2020-12-21
248	36	248	2020-12-21
249	36	249	2020-12-21
250	36	250	2020-12-21
252	36	252	2020-12-21
255	37	255	2020-12-21
256	37	256	2020-12-21
257	37	257	2020-12-21
259	37	259	2020-12-21
262	38	262	2020-12-21
263	38	263	2020-12-21
264	38	264	2020-12-21
266	38	266	2020-12-21
269	39	269	2020-12-21
270	39	270	2020-12-21
271	39	271	2020-12-21
273	39	273	2020-12-21
283	41	283	2020-12-21
284	41	284	2020-12-21
285	41	285	2020-12-21
287	41	287	2020-12-21
290	42	290	2020-12-21
291	42	291	2020-12-21
292	42	292	2020-12-21
707	3	712	2021-01-26
294	42	294	2020-12-21
297	43	297	2020-12-21
298	43	298	2020-12-21
299	43	299	2020-12-21
301	43	301	2020-12-21
304	44	304	2020-12-21
305	44	305	2020-12-21
306	44	306	2020-12-21
308	44	308	2020-12-21
311	45	311	2020-12-21
312	45	312	2020-12-21
313	45	313	2020-12-21
315	45	315	2020-12-21
318	46	318	2020-12-21
319	46	319	2020-12-21
320	46	320	2020-12-21
322	46	322	2020-12-21
325	47	325	2020-12-21
326	47	326	2020-12-21
327	47	327	2020-12-21
329	47	329	2020-12-21
332	48	332	2020-12-21
333	48	333	2020-12-21
334	48	334	2020-12-21
336	48	336	2020-12-21
339	49	339	2020-12-21
340	49	340	2020-12-21
341	49	341	2020-12-21
343	49	343	2020-12-21
353	51	353	2020-12-21
354	51	354	2020-12-21
355	51	355	2020-12-21
357	51	357	2020-12-21
360	52	360	2020-12-21
361	52	361	2020-12-21
362	52	362	2020-12-21
364	52	364	2020-12-21
367	53	367	2020-12-21
368	53	368	2020-12-21
369	53	369	2020-12-21
371	53	371	2020-12-21
374	54	374	2020-12-21
375	54	375	2020-12-21
376	54	376	2020-12-21
378	54	378	2020-12-21
381	55	381	2020-12-21
382	55	382	2020-12-21
383	55	383	2020-12-21
385	55	385	2020-12-21
388	56	388	2020-12-21
389	56	389	2020-12-21
390	56	390	2020-12-21
392	56	392	2020-12-21
395	57	395	2020-12-21
396	57	396	2020-12-21
397	57	397	2020-12-21
399	57	399	2020-12-21
402	58	402	2020-12-21
403	58	403	2020-12-21
404	58	404	2020-12-21
406	58	406	2020-12-21
409	59	409	2020-12-21
410	59	410	2020-12-21
411	59	411	2020-12-21
413	59	413	2020-12-21
416	60	416	2020-12-21
417	60	417	2020-12-21
418	60	418	2020-12-21
420	60	420	2020-12-21
423	61	423	2020-12-21
424	61	424	2020-12-21
425	61	425	2020-12-21
427	61	427	2020-12-21
430	62	430	2020-12-21
431	62	431	2020-12-21
432	62	432	2020-12-21
434	62	434	2020-12-21
437	63	437	2020-12-21
438	63	438	2020-12-21
708	3	713	2021-03-17
441	63	441	2020-12-21
444	64	444	2020-12-21
445	64	445	2020-12-21
446	64	446	2020-12-21
448	64	448	2020-12-21
451	65	451	2020-12-21
452	65	452	2020-12-21
453	65	453	2020-12-21
455	65	455	2020-12-21
458	66	458	2020-12-21
459	66	459	2020-12-21
460	66	460	2020-12-21
462	66	462	2020-12-21
465	67	465	2020-12-21
466	67	466	2020-12-21
467	67	467	2020-12-21
469	67	469	2020-12-21
472	68	472	2020-12-21
473	68	473	2020-12-21
474	68	474	2020-12-21
476	68	476	2020-12-21
479	69	479	2020-12-21
480	69	480	2020-12-21
481	69	481	2020-12-21
483	69	483	2020-12-21
486	70	486	2020-12-21
487	70	487	2020-12-21
488	70	488	2020-12-21
490	70	490	2020-12-21
493	71	493	2020-12-21
494	71	494	2020-12-21
495	71	495	2020-12-21
497	71	497	2020-12-21
500	72	500	2020-12-21
501	72	501	2020-12-21
502	72	502	2020-12-21
504	72	504	2020-12-21
507	73	507	2020-12-21
508	73	508	2020-12-21
509	73	509	2020-12-21
511	73	511	2020-12-21
514	74	514	2020-12-21
515	74	515	2020-12-21
516	74	516	2020-12-21
518	74	518	2020-12-21
521	75	521	2020-12-21
522	75	522	2020-12-21
523	75	523	2020-12-21
525	75	525	2020-12-21
528	76	528	2020-12-21
529	76	529	2020-12-21
530	76	530	2020-12-21
532	76	532	2020-12-21
535	77	535	2020-12-21
536	77	536	2020-12-21
537	77	537	2020-12-21
539	77	539	2020-12-21
542	78	542	2020-12-21
543	78	543	2020-12-21
544	78	544	2020-12-21
546	78	546	2020-12-21
549	79	549	2020-12-21
550	79	550	2020-12-21
551	79	551	2020-12-21
553	79	553	2020-12-21
556	80	556	2020-12-21
557	80	557	2020-12-21
558	80	558	2020-12-21
560	80	560	2020-12-21
563	81	563	2020-12-21
564	81	564	2020-12-21
565	81	565	2020-12-21
567	81	567	2020-12-21
570	82	570	2020-12-21
571	82	571	2020-12-21
572	82	572	2020-12-21
574	82	574	2020-12-21
577	83	577	2020-12-21
578	83	578	2020-12-21
579	83	579	2020-12-21
581	83	581	2020-12-21
584	84	584	2020-12-21
585	84	585	2020-12-21
586	84	586	2020-12-21
588	84	588	2020-12-21
591	85	591	2020-12-21
592	85	592	2020-12-21
593	85	593	2020-12-21
595	85	595	2020-12-21
598	86	598	2020-12-21
599	86	599	2020-12-21
600	86	600	2020-12-21
602	86	602	2020-12-21
605	87	605	2020-12-21
606	87	606	2020-12-21
607	87	607	2020-12-21
609	87	609	2020-12-21
612	88	612	2020-12-21
613	88	613	2020-12-21
614	88	614	2020-12-21
616	88	616	2020-12-21
619	89	619	2020-12-21
620	89	620	2020-12-21
621	89	621	2020-12-21
623	89	623	2020-12-21
626	90	626	2020-12-21
627	90	627	2020-12-21
628	90	628	2020-12-21
630	90	630	2020-12-21
633	91	633	2020-12-21
634	91	634	2020-12-21
635	91	635	2020-12-21
637	91	637	2020-12-21
640	92	640	2020-12-21
641	92	641	2020-12-21
642	92	642	2020-12-21
644	92	644	2020-12-21
647	93	647	2020-12-21
648	93	648	2020-12-21
649	93	649	2020-12-21
651	93	651	2020-12-21
654	94	654	2020-12-21
655	94	655	2020-12-21
656	94	656	2020-12-21
658	94	658	2020-12-21
661	95	661	2020-12-21
662	95	662	2020-12-21
663	95	663	2020-12-21
665	95	665	2020-12-21
668	96	668	2020-12-21
669	96	669	2020-12-21
670	96	670	2020-12-21
672	96	672	2020-12-21
675	97	675	2020-12-21
676	97	676	2020-12-21
677	97	677	2020-12-21
679	97	679	2020-12-21
682	98	682	2020-12-21
683	98	683	2020-12-21
684	98	684	2020-12-21
686	98	686	2020-12-21
689	99	689	2020-12-21
690	99	690	2020-12-21
691	99	691	2020-12-21
693	99	693	2020-12-21
696	100	696	2020-12-21
697	100	697	2020-12-21
698	100	698	2020-12-21
700	100	700	2020-12-21
\.


--
-- TOC entry 3033 (class 0 OID 0)
-- Dependencies: 202
-- Name: HealthParameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."HealthParameter_id_seq"', 26, true);


--
-- TOC entry 3034 (class 0 OID 0)
-- Dependencies: 204
-- Name: HealthValue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."HealthValue_id_seq"', 721, true);


--
-- TOC entry 3035 (class 0 OID 0)
-- Dependencies: 200
-- Name: Patient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Patient_id_seq"', 124, true);


--
-- TOC entry 3036 (class 0 OID 0)
-- Dependencies: 206
-- Name: patient_health_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patient_health_id_seq', 716, true);


--
-- TOC entry 2876 (class 2606 OID 16900)
-- Name: HealthParameter HealthParameter_denotation_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthParameter"
    ADD CONSTRAINT "HealthParameter_denotation_key" UNIQUE (denotation);


--
-- TOC entry 2878 (class 2606 OID 16898)
-- Name: HealthParameter HealthParameter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthParameter"
    ADD CONSTRAINT "HealthParameter_pkey" PRIMARY KEY (id);


--
-- TOC entry 2880 (class 2606 OID 16908)
-- Name: HealthValue HealthValue_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthValue"
    ADD CONSTRAINT "HealthValue_pkey" PRIMARY KEY (id);


--
-- TOC entry 2874 (class 2606 OID 16890)
-- Name: Patient Patient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Patient"
    ADD CONSTRAINT "Patient_pkey" PRIMARY KEY (id);


--
-- TOC entry 2882 (class 2606 OID 16921)
-- Name: patient_health patient_health_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_health
    ADD CONSTRAINT patient_health_pkey PRIMARY KEY (id);


--
-- TOC entry 2883 (class 2606 OID 16909)
-- Name: HealthValue HealthValue_parameter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."HealthValue"
    ADD CONSTRAINT "HealthValue_parameter_fkey" FOREIGN KEY (parameter) REFERENCES public."HealthParameter"(id);


--
-- TOC entry 2885 (class 2606 OID 16927)
-- Name: patient_health patient_health_healthvalue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_health
    ADD CONSTRAINT patient_health_healthvalue_id_fkey FOREIGN KEY (healthvalue_id) REFERENCES public."HealthValue"(id);


--
-- TOC entry 2884 (class 2606 OID 16922)
-- Name: patient_health patient_health_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient_health
    ADD CONSTRAINT patient_health_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public."Patient"(id);


-- Completed on 2021-01-26 21:37:00

--
-- PostgreSQL database dump complete
--

