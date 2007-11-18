--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.auth_message DROP CONSTRAINT user_id_refs_id_650f49a6;
ALTER TABLE ONLY public.main_page DROP CONSTRAINT main_page_category_id_fkey;
ALTER TABLE ONLY public.main_category DROP CONSTRAINT language_id_refs_id_224a59;
ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_site_id_fkey;
ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_flatpage_id_fkey;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_fkey;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_fkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT content_type_id_refs_id_728de91f;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_fkey;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_permission_id_fkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_fkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_permission_id_fkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_fkey;
DROP INDEX public.main_page_name;
DROP INDEX public.main_page_category_id;
DROP INDEX public.main_category_name;
DROP INDEX public.main_category_language_id;
DROP INDEX public.django_flatpage_url;
DROP INDEX public.django_admin_log_user_id;
DROP INDEX public.django_admin_log_content_type_id;
DROP INDEX public.auth_permission_content_type_id;
DROP INDEX public.auth_message_user_id;
ALTER TABLE ONLY public.ob_member DROP CONSTRAINT ob_member_pkey;
ALTER TABLE ONLY public.ob_competition DROP CONSTRAINT ob_competition_pkey;
ALTER TABLE ONLY public.ob_competition DROP CONSTRAINT ob_competition_name_key;
ALTER TABLE ONLY public.main_page DROP CONSTRAINT main_page_pkey;
ALTER TABLE ONLY public.main_page DROP CONSTRAINT main_page_name_key;
ALTER TABLE ONLY public.main_language DROP CONSTRAINT main_language_pkey;
ALTER TABLE ONLY public.main_language DROP CONSTRAINT main_language_code_key;
ALTER TABLE ONLY public.main_category DROP CONSTRAINT main_category_pkey;
ALTER TABLE ONLY public.django_site DROP CONSTRAINT django_site_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_pkey;
ALTER TABLE ONLY public.django_flatpage_sites DROP CONSTRAINT django_flatpage_sites_flatpage_id_key;
ALTER TABLE ONLY public.django_flatpage DROP CONSTRAINT django_flatpage_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_key;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_key;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_key;
ALTER TABLE ONLY public.auth_message DROP CONSTRAINT auth_message_pkey;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_key;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
ALTER TABLE public.ob_member ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.ob_competition ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.main_page ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.main_language ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.main_category ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_site ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_flatpage_sites ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_flatpage ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_message ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE public.ob_member_id_seq;
DROP TABLE public.ob_member;
DROP SEQUENCE public.ob_competition_id_seq;
DROP TABLE public.ob_competition;
DROP SEQUENCE public.main_page_id_seq;
DROP TABLE public.main_page;
DROP SEQUENCE public.main_language_id_seq;
DROP TABLE public.main_language;
DROP SEQUENCE public.main_category_id_seq;
DROP TABLE public.main_category;
DROP SEQUENCE public.django_site_id_seq;
DROP TABLE public.django_site;
DROP TABLE public.django_session;
DROP SEQUENCE public.django_flatpage_sites_id_seq;
DROP TABLE public.django_flatpage_sites;
DROP SEQUENCE public.django_flatpage_id_seq;
DROP TABLE public.django_flatpage;
DROP SEQUENCE public.django_content_type_id_seq;
DROP TABLE public.django_content_type;
DROP SEQUENCE public.django_admin_log_id_seq;
DROP TABLE public.django_admin_log;
DROP SEQUENCE public.auth_user_user_permissions_id_seq;
DROP TABLE public.auth_user_user_permissions;
DROP SEQUENCE public.auth_user_id_seq;
DROP SEQUENCE public.auth_user_groups_id_seq;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP SEQUENCE public.auth_permission_id_seq;
DROP TABLE public.auth_permission;
DROP SEQUENCE public.auth_message_id_seq;
DROP TABLE public.auth_message;
DROP SEQUENCE public.auth_group_permissions_id_seq;
DROP TABLE public.auth_group_permissions;
DROP SEQUENCE public.auth_group_id_seq;
DROP TABLE public.auth_group;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'Standard public schema';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO tjrapid;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO tjrapid;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO tjrapid;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO tjrapid;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_message; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_message (
    id integer NOT NULL,
    user_id integer NOT NULL,
    message text NOT NULL
);


ALTER TABLE public.auth_message OWNER TO tjrapid;

--
-- Name: auth_message_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_message_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_message_id_seq OWNER TO tjrapid;

--
-- Name: auth_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_message_id_seq OWNED BY auth_message.id;


--
-- Name: auth_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_message_id_seq', 208, true);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO tjrapid;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_permission_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO tjrapid;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    "password" character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO tjrapid;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO tjrapid;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO tjrapid;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_user_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO tjrapid;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO tjrapid;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO tjrapid;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO tjrapid;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE django_admin_log_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO tjrapid;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 208, true);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO tjrapid;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE django_content_type_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO tjrapid;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- Name: django_flatpage; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_flatpage (
    id integer NOT NULL,
    url character varying(100) NOT NULL,
    title character varying(200) NOT NULL,
    content text NOT NULL,
    enable_comments boolean NOT NULL,
    template_name character varying(70) NOT NULL,
    registration_required boolean NOT NULL
);


ALTER TABLE public.django_flatpage OWNER TO tjrapid;

--
-- Name: django_flatpage_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE django_flatpage_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_flatpage_id_seq OWNER TO tjrapid;

--
-- Name: django_flatpage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE django_flatpage_id_seq OWNED BY django_flatpage.id;


--
-- Name: django_flatpage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('django_flatpage_id_seq', 18, true);


--
-- Name: django_flatpage_sites; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_flatpage_sites (
    id integer NOT NULL,
    flatpage_id integer NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.django_flatpage_sites OWNER TO tjrapid;

--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE django_flatpage_sites_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_flatpage_sites_id_seq OWNER TO tjrapid;

--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE django_flatpage_sites_id_seq OWNED BY django_flatpage_sites.id;


--
-- Name: django_flatpage_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('django_flatpage_sites_id_seq', 77, true);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO tjrapid;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    "domain" character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO tjrapid;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE django_site_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO tjrapid;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Name: main_category; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE main_category (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    name character varying(50) NOT NULL,
    language_id integer NOT NULL,
    template_name character varying(100) NOT NULL,
    menu text NOT NULL
);


ALTER TABLE public.main_category OWNER TO tjrapid;

--
-- Name: main_category_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE main_category_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.main_category_id_seq OWNER TO tjrapid;

--
-- Name: main_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE main_category_id_seq OWNED BY main_category.id;


--
-- Name: main_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('main_category_id_seq', 10, true);


--
-- Name: main_language; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE main_language (
    id integer NOT NULL,
    code character varying(20) NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.main_language OWNER TO tjrapid;

--
-- Name: main_language_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE main_language_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.main_language_id_seq OWNER TO tjrapid;

--
-- Name: main_language_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE main_language_id_seq OWNED BY main_language.id;


--
-- Name: main_language_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('main_language_id_seq', 2, true);


--
-- Name: main_page; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE main_page (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    name character varying(50) NOT NULL,
    category_id integer NOT NULL,
    content text NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL
);


ALTER TABLE public.main_page OWNER TO tjrapid;

--
-- Name: main_page_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE main_page_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.main_page_id_seq OWNER TO tjrapid;

--
-- Name: main_page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE main_page_id_seq OWNED BY main_page.id;


--
-- Name: main_page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('main_page_id_seq', 15, true);


--
-- Name: ob_competition; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE ob_competition (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    name character varying(50) NOT NULL,
    start_date date NOT NULL,
    end_date date,
    "location" character varying(100) NOT NULL,
    specification character varying(200) NOT NULL,
    results character varying(200) NOT NULL,
    photos character varying(200) NOT NULL
);


ALTER TABLE public.ob_competition OWNER TO tjrapid;

--
-- Name: ob_competition_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE ob_competition_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.ob_competition_id_seq OWNER TO tjrapid;

--
-- Name: ob_competition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE ob_competition_id_seq OWNED BY ob_competition.id;


--
-- Name: ob_competition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('ob_competition_id_seq', 2, true);


--
-- Name: ob_member; Type: TABLE; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE TABLE ob_member (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    category character varying(5) NOT NULL,
    email character varying(75) NOT NULL
);


ALTER TABLE public.ob_member OWNER TO tjrapid;

--
-- Name: ob_member_id_seq; Type: SEQUENCE; Schema: public; Owner: tjrapid
--

CREATE SEQUENCE ob_member_id_seq
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.ob_member_id_seq OWNER TO tjrapid;

--
-- Name: ob_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tjrapid
--

ALTER SEQUENCE ob_member_id_seq OWNED BY ob_member.id;


--
-- Name: ob_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tjrapid
--

SELECT pg_catalog.setval('ob_member_id_seq', 5, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_message ALTER COLUMN id SET DEFAULT nextval('auth_message_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE django_flatpage ALTER COLUMN id SET DEFAULT nextval('django_flatpage_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE django_flatpage_sites ALTER COLUMN id SET DEFAULT nextval('django_flatpage_sites_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE main_category ALTER COLUMN id SET DEFAULT nextval('main_category_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE main_language ALTER COLUMN id SET DEFAULT nextval('main_language_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE main_page ALTER COLUMN id SET DEFAULT nextval('main_page_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE ob_competition ALTER COLUMN id SET DEFAULT nextval('ob_competition_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: tjrapid
--

ALTER TABLE ob_member ALTER COLUMN id SET DEFAULT nextval('ob_member_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_message; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_message (id, user_id, message) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add message	1	add_message
2	Can change message	1	change_message
3	Can delete message	1	delete_message
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add permission	4	add_permission
11	Can change permission	4	change_permission
12	Can delete permission	4	delete_permission
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add flat page	8	add_flatpage
23	Can change flat page	8	change_flatpage
24	Can delete flat page	8	delete_flatpage
25	Can add log entry	9	add_logentry
26	Can change log entry	9	change_logentry
27	Can delete log entry	9	delete_logentry
28	Can add page	10	add_page
29	Can change page	10	change_page
30	Can delete page	10	delete_page
31	Can add category	11	add_category
32	Can change category	11	change_category
33	Can delete category	11	delete_category
34	Can add language	12	add_language
35	Can change language	12	change_language
36	Can delete language	12	delete_language
37	Can add member	13	add_member
38	Can change member	13	change_member
39	Can delete member	13	delete_member
40	Can add competition	14	add_competition
41	Can change competition	14	change_competition
42	Can delete competition	14	delete_competition
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_user (id, username, first_name, last_name, email, "password", is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
1	peter	Peter	Kuma	peterkuma@waveland.org	sha1$9d080$1d9b8ef7d703f9766647307ec6b4fc1f1b6cb98d	t	t	t	2007-10-07 15:15:22.909986+01	2007-08-05 09:37:26+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2007-08-05 09:52:57.739045+01	1	7	1	tjrapid.sk	2	Bol zmenený názov domény a zobrazené meno
2	2007-08-05 09:53:23.998506+01	1	3	1	peter	2	Bol zmenený krstné meno, priezvisko, naposledy prihlásený a dátum registrácie
3	2007-08-05 10:03:46.606329+01	1	8	1	/ob/ -- Čo je OB?	1	
4	2007-08-05 10:07:59.721959+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený názov šablóny
5	2007-08-05 10:49:18.514875+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
6	2007-08-05 10:49:32.869574+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
7	2007-08-05 11:00:57.151771+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
8	2007-08-05 11:01:10.523506+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
9	2007-08-05 11:01:21.615807+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
10	2007-08-05 11:05:30.502776+01	1	8	2	/ob/menu/ -- OB (menu)	1	
11	2007-08-05 11:30:23.770981+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
12	2007-08-05 11:31:40.146457+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
13	2007-08-05 11:33:27.778238+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
14	2007-08-05 11:34:13.040386+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
15	2007-08-05 11:58:50.590983+01	1	8	2	/ob/menu/ -- Menu - OB	2	Bol zmenený názov
16	2007-08-05 11:58:57.758729+01	1	8	2	/ob/menu/ -- Menu OB	2	Bol zmenený názov
17	2007-08-05 11:59:14.18264+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený názov
18	2007-08-05 13:00:41.872064+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
19	2007-08-05 13:00:53.848732+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
20	2007-08-05 13:57:31.832695+01	1	8	3	/ -- Hlavná stránka	1	
21	2007-08-05 14:09:15.806223+01	1	8	3	/ -- Hlavná stránka	2	Bol zmenený názov šablóny
22	2007-08-05 14:12:16.020219+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
23	2007-08-05 14:12:23.099682+01	1	8	2	/ob/menu/ -- OB (menu)	2	Bol zmenený obsah
24	2007-08-05 14:24:27.699135+01	1	8	3	/ -- Hlavná stránka	2	Bol zmenený obsah
25	2007-08-05 14:24:41.313476+01	1	8	3	/ -- Hlavná stránka	2	Bol zmenený obsah
26	2007-08-05 14:24:58.99062+01	1	8	3	/ -- Hlavná stránka	2	Bol zmenený obsah
27	2007-08-05 14:34:07.91463+01	1	8	4	/hadzana/ -- Úvod	1	
28	2007-08-05 14:34:18.542947+01	1	8	4	/hadzana/ -- Úvod	2	Bol zmenený názov šablóny
29	2007-08-05 14:42:13.148021+01	1	8	5	/hadzana/menu/ -- Menu	1	
30	2007-08-05 14:42:28.989949+01	1	8	2	/ob/menu/ -- Menu	2	Bol zmenený názov
31	2007-08-05 14:45:27.603723+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
32	2007-08-05 15:04:05.583752+01	1	8	6	/karate/menu -- Menu	1	
33	2007-08-05 15:04:19.207641+01	1	8	6	/karate/menu/ -- Menu	2	Bol zmenený URL
34	2007-08-05 15:05:11.220591+01	1	8	7	/karate/ -- Úvod	1	
35	2007-08-05 15:05:21.949606+01	1	8	7	/karate/ -- Úvod	2	Bol zmenený názov šablóny
36	2007-08-05 15:06:38.514848+01	1	8	7	/karate/ -- Úvod	2	Bol zmenený obsah
37	2007-08-05 15:08:12.380938+01	1	8	7	/karate/ -- Úvod	2	Bol zmenený obsah
38	2007-08-05 15:08:31.887966+01	1	8	7	/karate/ -- Úvod	2	Bol zmenený obsah
39	2007-08-05 15:09:11.764003+01	1	8	4	/hadzana/ -- Úvod	2	Bol zmenený obsah
40	2007-08-05 15:09:24.686223+01	1	8	4	/hadzana/ -- Úvod	2	Bol zmenený obsah
41	2007-08-05 15:10:41.278136+01	1	8	8	/cyklo/menu/ -- Menu	1	
42	2007-08-05 15:12:21.431839+01	1	8	9	/cyklo/ -- Úvod	1	
43	2007-08-05 15:13:30.542174+01	1	8	8	/cyklo/menu/ -- Menu	2	Bol zmenený obsah
44	2007-08-05 15:14:47.259777+01	1	8	10	/turistika/menu/ -- Menu	1	
45	2007-08-05 15:15:20.859556+01	1	8	11	/turistika/ -- Úvod	1	
46	2007-08-05 15:18:44.615234+01	1	8	12	/gymnastika/menu/ -- Menu	1	
47	2007-08-05 15:20:17.918314+01	1	8	13	/gymnastika/ -- Úvod	1	
48	2007-08-05 15:20:24.939175+01	1	8	12	/gymnastika/menu/ -- Menu	2	Bol zmenený názov šablóny
49	2007-08-05 15:22:20.777311+01	1	8	13	/gymnastika/ -- Úvod	2	Bol zmenený obsah
50	2007-08-05 15:25:33.824504+01	1	8	14	/gymnastika/fotografie/ -- Fotografie	1	
51	2007-08-05 15:26:44.63715+01	1	8	14	/gymnastika/fotografie/ -- Fotografie	2	Bol zmenený obsah
52	2007-08-05 15:38:19.617097+01	1	8	4	/hadzana/ -- Úvod	2	Bol zmenený obsah
53	2007-08-05 15:38:38.434367+01	1	8	7	/karate/ -- Úvod	2	Bol zmenený obsah
54	2007-08-05 15:38:53.018057+01	1	8	9	/cyklo/ -- Úvod	2	Bol zmenený obsah
55	2007-08-05 15:47:45.546185+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
56	2007-08-05 15:48:11.604719+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
57	2007-08-05 15:48:21.741536+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
58	2007-08-05 15:54:35.116881+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
59	2007-08-05 15:55:42.075885+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
60	2007-08-05 15:55:57.2123+01	1	8	1	/ob/ -- Čo je OB?	2	Bol zmenený obsah
61	2007-08-05 16:00:23.954219+01	1	8	1	/ob/ -- Čo je OB?	2	Polia neboli zmenené.
62	2007-08-05 16:03:30.684557+01	1	8	15	/ob/vybor/ -- Výbor oddielu	1	
63	2007-08-05 16:04:35.725321+01	1	8	15	/ob/vybor/ -- Výbor oddielu	2	Bol zmenený obsah
64	2007-08-05 17:27:34.686643+01	1	8	14	/gymnastika/fotografie/ -- Fotografie	2	Bol zmenený obsah
65	2007-08-05 17:50:30.702831+01	1	8	15	/ob/vybor/ -- Výbor oddielu	2	Bol zmenený obsah
66	2007-08-05 17:52:52.835462+01	1	8	15	/ob/vybor/ -- Výbor oddielu	2	Bol zmenený obsah
67	2007-08-05 17:55:31.006305+01	1	8	16	/ob/historia -- História oddielu	1	
68	2007-08-05 17:55:45.099269+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený URL
69	2007-08-05 18:20:54.087137+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený obsah
70	2007-08-05 18:21:12.243586+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený obsah
71	2007-08-05 18:21:44.978026+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený obsah
72	2007-08-05 18:22:38.554669+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený obsah
73	2007-08-05 18:23:01.385805+01	1	8	16	/ob/historia/ -- História oddielu	2	Bol zmenený obsah
74	2007-08-05 18:28:14.028379+01	1	8	17	/ob/linky/ -- WWW linky	1	
75	2007-08-05 18:28:23.510044+01	1	8	18	/ob/linky/ -- WWW linky	1	
76	2007-08-05 18:28:48.244981+01	1	8	17	/ob/linky/ -- WWW linky	3	
77	2007-08-05 18:31:18.819219+01	1	8	18	/ob/linky/ -- WWW linky	2	Bol zmenený obsah
78	2007-08-05 18:32:29.027669+01	1	8	18	/ob/linky/ -- WWW linky	2	Bol zmenený obsah
79	2007-08-05 18:32:40.220291+01	1	8	18	/ob/linky/ -- WWW linky	2	Bol zmenený obsah
80	2007-08-05 18:34:35.246048+01	1	8	18	/ob/linky/ -- WWW linky	2	Bol zmenený obsah
81	2007-09-15 11:37:37.284204+01	1	11	1	Category object	1	
82	2007-09-15 11:38:35.94075+01	1	11	2	Hádzaná	1	
83	2007-09-15 11:38:48.238122+01	1	11	3	Karate	1	
84	2007-09-15 11:39:01.908839+01	1	11	4	Moderná gymnastika	1	
85	2007-09-15 11:39:12.662051+01	1	11	5	Orientačný beh	1	
86	2007-09-15 11:39:22.453919+01	1	11	6	Turistika	1	
87	2007-09-15 11:53:07.802442+01	1	11	1	Cyklistika	2	Bol zmenený template name
88	2007-09-15 11:53:13.839834+01	1	11	2	Hádzaná	2	Bol zmenený template name
89	2007-09-15 11:53:19.230494+01	1	11	3	Karate	2	Bol zmenený template name
90	2007-09-15 11:53:31.569336+01	1	11	4	Moderná gymnastika	2	Bol zmenený template name
91	2007-09-15 11:53:33.734917+01	1	11	5	Orientačný beh	2	Polia neboli zmenené.
92	2007-09-15 11:53:42.646354+01	1	11	6	Turistika	2	Bol zmenený template name
93	2007-09-15 12:53:00.387388+01	1	10	3	Orientačný beh - WWW Linky	1	
94	2007-09-15 12:53:08.418105+01	1	10	3	Orientačný beh - WWW Linky	2	Bol zmenený modified
95	2007-09-15 13:18:22.65756+01	1	8	18	/ob/linky/ -- WWW linky	3	
96	2007-09-15 14:04:13.553699+01	1	10	1	Orientačný beh -- Čo je OB	2	Bol zmenený názov a modified
97	2007-09-15 14:04:29.181452+01	1	10	1	Orientačný beh -- Čo je OB?	2	Bol zmenený názov a modified
98	2007-09-15 14:04:59.719079+01	1	8	1	/ob/ -- Čo je OB?	3	
99	2007-09-15 14:07:09.674271+01	1	10	4	Cyklistika -- Úvod	1	
100	2007-09-15 14:07:43.395457+01	1	8	9	/cyklo/ -- Úvod	3	
101	2007-09-15 14:08:07.94405+01	1	10	5	Moderná gymnastika -- Úvod	1	
102	2007-09-15 14:08:26.430076+01	1	8	13	/gymnastika/ -- Úvod	3	
103	2007-09-15 14:08:58.111428+01	1	10	6	Moderná gymnastika -- Fotografie	1	
104	2007-09-15 14:09:16.739527+01	1	8	14	/gymnastika/fotografie/ -- Fotografie	3	
105	2007-09-15 14:09:38.070934+01	1	10	7	Hádzaná -- Úvod	1	
106	2007-09-15 14:09:41.739253+01	1	8	4	/hadzana/ -- Úvod	3	
107	2007-09-15 14:10:02.956335+01	1	10	8	Karate -- Úvod	1	
108	2007-09-15 14:10:37.982956+01	1	8	7	/karate/ -- Úvod	3	
109	2007-09-15 14:11:15.105172+01	1	10	9	Orientačný beh -- História oddielu	1	
110	2007-09-15 14:11:22.564842+01	1	8	16	/ob/historia/ -- História oddielu	3	
111	2007-09-15 14:11:42.559612+01	1	10	10	Orientačný beh -- Výbor oddielu	1	
112	2007-09-15 14:11:54.699123+01	1	8	15	/ob/vybor/ -- Výbor oddielu	3	
113	2007-09-15 14:12:12.317719+01	1	10	11	Turistika -- Úvod	1	
114	2007-09-15 14:12:17.282917+01	1	8	11	/turistika/ -- Úvod	3	
115	2007-09-15 15:16:17.774262+01	1	11	1	Cyklistika	2	Polia neboli zmenené.
116	2007-09-15 15:16:37.720783+01	1	12	2	English	1	
117	2007-09-15 16:33:13.847919+01	1	11	7	Orienteering	1	
118	2007-09-15 16:33:38.7407+01	1	12	2	English	2	Bol zmenený code
119	2007-09-15 16:33:45.542355+01	1	12	2	English	2	Bol zmenený code
120	2007-09-15 16:37:35.018148+01	1	10	32	Cyklistika -- Úvod	2	Bol zmenený meno a modified
121	2007-09-15 16:37:47.10961+01	1	10	32	Cyklistika -- Úvod	2	Bol zmenený modified
122	2007-09-15 16:39:54.369122+01	1	10	28	Karate -- Úvod	2	Bol zmenený modified
123	2007-09-15 16:41:11.878149+01	1	10	28	Karate -- Úvod	2	Bol zmenený modified
124	2007-09-15 16:41:26.703536+01	1	10	28	Hádzaná -- Úvod	2	Bol zmenený category a modified
125	2007-09-15 16:44:32.824613+01	1	10	23	Turistika -- WWW Linky	2	Bol zmenený modified
126	2007-09-15 16:44:42.564642+01	1	10	23	Orientačný beh -- WWW Linky	2	Bol zmenený category a modified
127	2007-09-15 16:46:30.405861+01	1	10	31	Orientačný beh -- Výbor oddielu	2	Bol zmenený category a modified
128	2007-09-15 16:46:39.637085+01	1	10	30	Orientačný beh -- História oddielu	2	Bol zmenený category a modified
129	2007-09-15 16:47:03.42804+01	1	10	26	Moderná gymnastika -- Úvod	2	Bol zmenený category a modified
130	2007-09-15 16:47:15.949473+01	1	10	29	Karate -- Úvod	2	Bol zmenený meno, category a modified
131	2007-09-15 16:47:46.755536+01	1	10	32	Cyklistika -- Úvod	2	Bol zmenený meno a modified
132	2007-09-15 16:47:57.517494+01	1	10	25	Cyklistika -- Úvod	2	Bol zmenený category a modified
133	2007-09-15 16:48:08.041538+01	1	10	32	Turistika -- Úvod	2	Bol zmenený category a modified
134	2007-09-15 16:48:17.185512+01	1	10	24	Orientačný beh -- Čo je OB?	2	Bol zmenený category a modified
135	2007-09-15 16:48:33.00893+01	1	10	32	Turistika -- Úvod	2	Bol zmenený meno a modified
136	2007-09-15 16:49:07.662001+01	1	10	28	Hádzaná -- Úvod	2	Bol zmenený meno a modified
137	2007-09-15 17:14:02.224252+01	1	12	1	Slovensky	1	
138	2007-09-15 17:14:08.133085+01	1	12	2	English	1	
139	2007-09-15 17:14:33.666023+01	1	11	1	Orientačný beh	1	
140	2007-09-15 17:15:28.134428+01	1	10	1	Orientačný beh -- Čo je OB?	1	
141	2007-09-15 17:18:31.949531+01	1	10	1	Orientačný beh -- Čo je OB?	2	Bol zmenený obsah a modified
142	2007-09-15 17:23:33.137893+01	1	11	1	Orientačný beh	2	Bol zmenený menu
143	2007-09-15 17:24:51.93579+01	1	11	1	Orientačný beh	2	Bol zmenený menu
144	2007-09-15 17:25:39.316725+01	1	11	1	Orientačný beh	2	Bol zmenený menu
145	2007-09-15 17:42:23.12045+01	1	12	1	Slovensky	2	Polia neboli zmenené.
146	2007-09-15 19:50:21.775624+01	1	11	2	Hlavná	1	
147	2007-09-15 19:53:32.249406+01	1	11	3	Hlavná	1	
148	2007-09-15 19:53:53.493345+01	1	11	2	Hlavná	3	
149	2007-09-15 20:02:52.816793+01	1	11	4	Main	1	
150	2007-09-15 20:03:22.564381+01	1	11	5	Orienteering	1	
151	2007-09-15 20:08:50.475626+01	1	10	2	Main -- What is orienteering?	1	
152	2007-09-15 20:14:24.045988+01	1	10	3	Orientačný beh -- WWW Linky	1	
153	2007-09-15 20:34:08.699667+01	1	10	2	Orienteering -- What is orienteering?	2	Bol zmenený category a modified
154	2007-09-15 20:39:49.212512+01	1	10	2	Orienteering -- Welcome!	2	Bol zmenený názov, obsah a modified
155	2007-09-15 20:40:44.615458+01	1	10	2	Orienteering -- Welcome!	2	Bol zmenený obsah a modified
156	2007-09-15 20:44:16.332691+01	1	11	5	Orienteering (en-us)	2	Bol zmenený menu
157	2007-09-15 21:20:29.791238+01	1	11	5	Orienteering (en-us)	2	Bol zmenený menu
158	2007-09-15 21:20:47.165149+01	1	12	1	Slovensky	2	Bol zmenený code
159	2007-09-15 21:20:50.065289+01	1	12	1	Slovensky	2	Polia neboli zmenené.
160	2007-09-15 21:20:55.518068+01	1	12	2	English	2	Bol zmenený code
161	2007-09-15 21:30:33.0228+01	1	10	2	Orienteering -- Welcome!	2	Bol zmenený modified
162	2007-09-22 20:07:22.770099+01	1	13	3	Iva Kumová	1	
163	2007-09-22 20:07:28.995053+01	1	13	2	Iva Kumová	3	
164	2007-09-22 20:07:32.331958+01	1	13	3	Iva Kumová	3	
165	2007-09-22 20:13:03.3021+01	1	13	4	Jakub Schenk	1	
166	2007-09-22 20:13:47.783847+01	1	13	5	Túró Tomáš	1	
167	2007-09-22 22:07:12.320446+01	1	10	4	Orientačný beh -- História oddielu	1	
168	2007-09-22 22:08:30.521672+01	1	10	5	Orientačný beh -- Výbor oddielu	1	
169	2007-09-22 22:11:29.361987+01	1	11	1	Orientačný beh (sk)	2	Bol zmenený menu
170	2007-09-22 22:14:53.530429+01	1	10	6	Orientačný beh -- Mapy	1	
171	2007-09-22 22:15:25.874913+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
172	2007-09-22 22:17:37.725875+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
173	2007-09-22 22:17:51.761257+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
174	2007-09-22 22:51:48.068282+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
175	2007-09-22 22:52:35.042641+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
176	2007-09-22 22:53:12.536117+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
177	2007-09-22 22:53:27.06808+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
178	2007-09-22 22:54:00.685587+01	1	10	6	Orientačný beh -- Mapy	2	Bol zmenený obsah a modified
179	2007-09-22 23:48:11.361333+01	1	14	2	Competition object	1	
180	2007-09-22 23:51:56.897621+01	1	14	1	Competition object	1	
181	2007-10-01 23:16:36.01422+01	1	14	1	Competition object	1	
182	2007-10-01 23:17:11.180828+01	1	14	2	Competition object	1	
183	2007-10-02 00:32:56.46653+01	1	14	1	Competition object	2	Bol zmenený specification
184	2007-10-02 00:33:07.734234+01	1	14	2	Competition object	2	Bol zmenený specification
185	2007-10-02 01:08:50.674595+01	1	14	2	Competition object	2	Bol zmenený results
186	2007-10-02 01:10:12.912209+01	1	14	2	Competition object	2	Bol zmenený photos
187	2007-10-05 00:41:10.31978+01	1	11	6	Cyklistika (sk)	1	
188	2007-10-05 00:41:36.884664+01	1	11	7	Hádzaná (sk)	1	
189	2007-10-05 00:42:04.986047+01	1	11	8	Karate (sk)	1	
190	2007-10-05 00:42:43.918232+01	1	11	9	Moderná gymnastika (sk)	1	
191	2007-10-05 00:43:10.509924+01	1	11	10	Turistika (sk)	1	
192	2007-10-05 00:44:56.863808+01	1	10	7	Cyklistika -- Úvod	1	
193	2007-10-05 00:45:25.968041+01	1	11	6	Cyklistika (sk)	2	Bol zmenený meno
194	2007-10-05 00:46:15.512769+01	1	10	8	Moderná gymnastika -- Úvod	1	
195	2007-10-05 00:46:45.928272+01	1	10	9	Moderná gymnastika -- Fotografie	1	
196	2007-10-05 00:47:31.820874+01	1	10	10	Hádzaná -- Úvod	1	
197	2007-10-05 00:47:53.326034+01	1	10	11	Karate -- Karate	1	
198	2007-10-05 00:48:17.75699+01	1	10	12	Turistika -- Úvod	1	
199	2007-10-05 00:49:08.446656+01	1	10	9	Moderná gymnastika -- Fotografie	2	Bol zmenený meno a modified
200	2007-10-05 00:49:35.948466+01	1	11	10	Turistika (sk)	2	Bol zmenený názov šablóny
201	2007-10-05 00:50:50.079164+01	1	11	6	Cyklistika (sk)	2	Bol zmenený meno
202	2007-10-05 00:59:07.342633+01	1	10	13	Orienteering -- About	1	
203	2007-10-05 01:14:34.699781+01	1	10	13	Orienteering -- About	2	Bol zmenený modified
204	2007-10-05 01:15:52.888874+01	1	10	14	Orienteering -- Committee	1	
205	2007-10-05 01:28:43.13101+01	1	10	15	Orienteering -- Maps	1	
206	2007-10-05 01:30:09.500393+01	1	10	15	Orienteering -- Maps	2	Bol zmenený obsah a modified
207	2007-10-05 01:31:12.220058+01	1	10	15	Orienteering -- Maps	2	Bol zmenený obsah a modified
208	2007-10-05 01:32:34.53893+01	1	10	14	Orienteering -- Committee	2	Bol zmenený obsah a modified
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	message	auth	message
2	group	auth	group
3	user	auth	user
4	permission	auth	permission
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	flat page	flatpages	flatpage
9	log entry	admin	logentry
10	page	main	page
11	category	main	category
12	language	main	language
13	member	ob	member
14	competition	ob	competition
\.


--
-- Data for Name: django_flatpage; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_flatpage (id, url, title, content, enable_comments, template_name, registration_required) FROM stdin;
3	/	Hlavná stránka	h2. Vitajte!\r\n\r\nTelovýchovná jednota Rapid Bratislava vznikla v roku 1931 v zaostalej periférnej štvrti Prievoz. V tomto období mala TJ iba 200 členov registrovaných v troch oddieloch. Výrazný vzostup zaznamenala po roku 1948, kedy sa zlepšili podmienky pre športovanie a TJ evidovala 11 oddielov s 1936 členmi.\r\n\r\n<div class="pic-right"><img src="/site_media/upload/foto.jpg" /></div>\r\n\r\nNa fotografii členovia Výboru TJ Rapid Bratislava, zľava:\r\nDušan Formanko - podpredseda TJ (orientačný beh), Karol Menschy - člen (cyklistika),\r\nMarta Borovská - členka (moderná gymnastika), Ján Longa - predseda TJ (karate),\r\nVlasta Haplová - členka (sekretariát), Milan Bujalka - člen (hádzaná), Jozef Kubíček - člen\r\n(turistika).\r\n\r\nDnes má telovýchovná jednota vo svojich radoch 407 členov v šiestich oddieloch:\r\ncyklistika,  hádzaná,  moderná gymnastika,  karate,  orientačný beh  a  turistika.\r\n\r\nNaši športovci úspešne súťažia na domácich aj zahraničných súťažiach. TJ Rapid Bratislava má aj svoje hospodárske zariadenie a podniká v prenájme vlastných kancelárskych, skladových a otvorených priestorov. Prevádzkuje aj zariadenie pre tipujúcich - stávkovú zberňu na Herlianskej ul. v Bratislave, kde sprostredkováva hry Športka, Keno 10, Mates a predaj žrebov.	f	main.html	f
2	/ob/menu/	Menu	* "Čo je OB?":/ob/\r\n* "Členovia oddielu":/ob/clenovia/\r\n* "História oddielu":/ob/historia/\r\n* "Naše preteky":/ob/preteky/\r\n* "Výbor oddielu":/ob/vybor/\r\n* "Fotky":/ob/fotky/\r\n* "Mapy":/ob/mapy/\r\n* "WWW linky":/ob/linky/	f		f
5	/hadzana/menu/	Menu	* "Úvod":/hadzana/	f		f
6	/karate/menu/	Menu	* "Úvod":/karate/uvod/	f	karate.html	f
8	/cyklo/menu/	Menu	* "Úvod":/cyklo/	f		f
10	/turistika/menu/	Menu	* "Úvod":/turistika/	f		f
12	/gymnastika/menu/	Menu	* "Úvod":/gymnastika/\r\n* "Fotografie":/gymnastika/fotografie/	f		f
\.


--
-- Data for Name: django_flatpage_sites; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_flatpage_sites (id, flatpage_id, site_id) FROM stdin;
24	3	1
27	5	1
28	2	1
31	6	1
41	8	1
42	10	1
46	12	1
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
54607d6b26e9e4dbd4087b62570aedd5	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-08-19 09:52:37.377113+01
2563db9cf0f958a520dd069c6de53f5b	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-09-28 22:54:44.789653+01
eb4faef895744ffbac285b5869979674	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-10-06 19:22:59.65627+01
aa219e98802c264bb2bd41fec1f334c3	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-10-15 23:14:58.520787+01
006dc1b39a4738dcf44bc4de1566ae1a	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-10-19 00:40:17.291548+01
8ccf771da51bbbe545b818849a65e00e	KGRwMQpTJ19hdXRoX3VzZXJfYmFja2VuZCcKcDIKUydkamFuZ28uY29udHJpYi5hdXRoLmJhY2tl\nbmRzLk1vZGVsQmFja2VuZCcKcDMKc1MnX2F1dGhfdXNlcl9pZCcKcDQKSTEKcy5iODRmOTczMDkw\nZWU1YmE2N2NlNDQ3MzUxN2I2YTBkOQ==\n	2007-10-21 15:15:22.966591+01
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY django_site (id, "domain", name) FROM stdin;
1	tjrapid.sk	tjrapid.sk
\.


--
-- Data for Name: main_category; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY main_category (id, title, name, language_id, template_name, menu) FROM stdin;
3	Hlavná		1	main.html	
4	Main		2	main.html	
5	Orienteering	orienteering	2	ob.html	* "Introduction":/en/orienteering/\r\n* "About Us":/en/orienteering/about/\r\n* "Committee":/en/orienteering/committee/\r\n* "Members":/en/orienteering/members/\r\n* "Competitions":/en/orienteering/competitions/\r\n* "Maps":/en/orienteering/maps
1	Orientačný beh	ob	1	ob.html	* "Čo je OB?":/ob/\r\n* "Členovia oddielu":/ob/clenovia/\r\n* "História oddielu":/ob/historia/\r\n* "Naše preteky":/ob/preteky/\r\n* "Výbor oddielu":/ob/vybor/\r\n* "Fotky":http://vcielka.rec.uniba.sk/~peter/tjrapid/\r\n* "Mapy":/ob/mapy/\r\n* "WWW linky":/ob/linky/
7	Hádzaná	hadzana	1	hadzana.html	* "Úvod":/hadzana/
8	Karate	karate	1	karate.html	* "Úvod":/karate/uvod/
9	Moderná gymnastika	gymnastika	1	gymnastika.html	* "Úvod":/gymnastika/\r\n* "Fotografie":/gymnastika/fotografie/
10	Turistika	turistika	1	turistika.html	* "Úvod":/turistika/
6	Cyklistika	cyklo	1	cyklo.html	* "Úvod":/cyklo/
\.


--
-- Data for Name: main_language; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY main_language (id, code, name) FROM stdin;
1	sk	Slovensky
2	en	English
\.


--
-- Data for Name: main_page; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY main_page (id, title, name, category_id, content, created, modified) FROM stdin;
1	Čo je OB?		1	Orientačný beh je svojím charakterom a rozsahom šport pre všetkých, šport moderný, dynamický, nenáročný s vysokým kondičným a relaxačným účinkom, maximálne spojený s prírodou. Kategórie sú prispôsobené veku a pohlaviu dĺžkou trate a orientačnou náročnosťou. Vekové kategórie začínajú od 10 ročných detí až po tých skôr narodených v kategórii nad 65 rokov.\r\n\r\nÚlohou pretekára, ktorý po štarte dostane mapu, je absolvovať čo najrýchlejšie trať zakreslenú v mape. Trať sa skladá z kontrolných stanovíšť, ktoré musí pretekár v lese nájsť v predpísanom poradí, pričom si samostatne volí postup v teréne. Povolená pomôcka je buzola. Víťazí pretekár s najnižším časom. "Pravidlá OB":/site_media/upload/ob/PravidlaOB.pdf, "Rady začiatočníkom":/site_media/upload/ob/RadyZaciatocnikom.pdf.\r\n\r\nNa Slovensku je zaregistrovaných 35 klubov a oddielov orientačného behu, ktoré sú združené v "Slovenskom zväze orientačných športov":http://www.orienteering.sk, členská základňa je 650 členov. SZOŠ organizuje súťaže vo všetkých druhoch orientácie - denný OB, nočný OB, lyžiarsky OB a orientačnú cyklistiku. Verím, že Vás uvedené informácie zaujali a nezostanú bez odozvy. Teším sa na osobné stretnutie s Vami pri pretekoch, či už v diváckej kulise alebo v pretekárskom poli.\r\nS pozdravom „Správny smer!"\r\n\r\np>.\r\n*Dušan Formanko*\r\n*predseda oddielu OB*\r\n*TJ Rapid Bratislava*	2007-09-15 17:15:28.124799+01	2007-09-15 17:18:31.939178+01
3	WWW Linky	linky	1	h4. Zväzy orientačného behu\r\n\r\n* "Slovenský zväz orientačného behu":http://www.orienteering.sk\r\n* "Český svaz orientačního běhu":http://www.orientacnibeh.cz\r\n* "International Orienteering Federation":http://www.orienteering.org/i3/index.php?/iof2006\r\n\r\nh4. Počasie\r\n\r\n* <a href="http://www.shmu.sk">Slovenský hydrometeorologický ústav</a>\r\n* <a href="http://www.chmi.sk">Český hydrometeorologický ústav</a>\r\n\r\nh4. Športové potreby pre OB\r\n\r\n* <a href="http://www.shop.orienteering.cz">Obuv, dresy, buzoly</a>\r\n* <a href="http://www.hedva.cz/prodej/?welen-dederon">Dederon-látky</a>	2007-09-15 20:14:24.035653+01	2007-09-15 20:14:24.035683+01
2	Welcome!		5	Orienteering is a sport for everybody by its character and extent. The sport is modern, dynamic, easy with high effect on physical condition and relaxation, moreover completely connected with nature. The age does not affect, flexibility for every age according to category, gender, distance and level of orientation. The age categories are divided from age of 10 to category – over 65 years old - the early born.\r\nThe task for every participant after getting a detailed map by the start is to absolve a course drawn on the map in the shortest time. The course is built on control points, which participant has to find in the forest while she/he is choosing the best route in terrain. The winner is a runner with the best time.\r\n\r\nIn Slovakia, there are registered 35 clubs and teams in foot-orienteering that are federated in SLOVENSKY ZVAZ ORIENTACNYCH SPORTOV (SZOS) with 650 members. SZOS organize the competitions in all kind of orienteering – day/night foot-orienteering, ski-orienteering and mountain-bike-orienteering.\r\nI hope this information interested you and you will not let it be without feedback. I’m looking forward to meet you personally neither among the by-standing people or in competing field. With salutation: ‘Right direction’\r\n\r\np>.\r\n*Dušan Formanko*\r\n*Head of Foot-orienteering Club*\r\n*TJ Rapid Bratislava*	2007-09-15 20:08:50.468937+01	2007-09-15 21:30:33.015937+01
4	História oddielu	historia	1	Náš oddiel OB patrí k prvým oddielom so zameraním na orientačný beh, ktoré vznikali vo vtedajšom Československu. Skupina nadšencov a vyznávačov tohto športu zo Slávie SVŠT a Lokomotívy Bratislava sa rozhodli hľadať lepšie podmienky na rozvoj svojej činnosti a v roku 1966 založila Oddiel orientačného behu pri TJ Rapid Bratislava. Prvým predsedom oddielu sa stal Ing. Mojmír Šeliga. Dosiahnuté výsledky z tohto obdobia ukazujú, že v TJ Rapid našli výborné podmienky na tréning i vrcholový šport.\r\n\r\n<a href="/site_media/upload/ob/historia/big/ob1.jpg"><img src="/site_media/upload/ob/historia/small/ob1.jpg" alt="" class="pic-right" /></a>\r\n\r\nPre ilustráciu:\r\nr.1967 Majstrovstvá ČSSR - Ľ. Šmelík 3.miesto\r\nr.1968 Majstrovstvá ČSSR - Ľ. Šmelík 1.miesto, Majstrovstvá Slovenska - Ľ. Šmelík 1.miesto, O.Vigašová - 1.miesto\r\nr.1969 Majstrovstvá Slovenska - štafeta (Ľ. Šmelík, L. Hýbal, J. Jašek) - 1. miesto\r\nr.1970 Slovenský rebríček - Ľ Šmelík 1. miesto, Čs. rebríček družstiev - TJ Rapid 6. miesto\r\nr.1971 Slovenský rebríček - P. Sláma 1. miesto, Ľ. Šmelík 2. Miesto\r\nr.1972 Slovenský rebríček - Ľ. Šmelík 1. Miesto, Majstrovstvá Slovenska - štafeta mužov 1. miesto\r\n\r\nOrientační bežci z TJ Rapid Bratislava boli úspešní nielen po športovej a výkonnostnej stránke, ale angažovali sa a boli priekopníci aj v iných oblastiach tohto športu. V r.1968 iniciovali vznik Zväzu orientačného behu Slovenska a jeho predsedom sa stal „rapiďák“ Ing. Mojmír Šeliga. Nezaostala ani organizačná činnosť a poriadanie pretekov. Oddiel zorganizoval športový pobyt v Mekke orientačného behu vo Švédsku, podarilo sa zrealizovať myšlienku viacdenných medzinárodných pretekov a tak v r.1971 poriadal náš oddiel 1. ročník trojdenných medzinárodných pretekov Grand Prix Slovakia na mapách Zurdok, Ravnica a Kamzík. Usporiadali sme i 3. ročník Grand prix Slovakia na mapách Pekný les, Vetrov plac a Kamzík.\r\n\r\n\r\n<a href="/site_media/upload/ob/historia/big/ob2.jpg"><img src="/site_media/upload/ob/historia/small/ob2.jpg" alt="" class="pic-left" /></a>\r\n\r\nALT Ďalšia tradičná akcia začala v r.1973 -1. ročník pretekov Prvý jarný kufor, ktoré sa konajú každoročne doteraz. Niekoľkokrát sme usporiadali i najvyššie domáce preteky, Majstrovstvá ČSSR, a to v r.1974-klasická trať a štafety, r.1977-dlhá trať (mapa Červený kameň), r.1983-dlhá trať (mapa Lažetky 1, 2, 3), r.1985-klasická trať a štafety (mapy Stánisko a Kačín).\r\n\r\nOd roku 1976 riadil činnosť oddielu OB nový predseda oddielu - Viktor Vávra. V tomto období bol príliv talentovaných detí, z ktorých mnohé zostali verné OB dodnes. Napr. V. Autrata, bratia Petrincovci, A. Kľučková, E. Pukalovičová, sestry Lukáškové, P. Sláma ml. a ďalší.\r\n\r\n<a href="/site_media/upload/ob/historia/big/ob3.jpg"><img src="/site_media/upload/ob/historia/small/ob3.jpg" alt="" class="pic-right" /></a>\r\n\r\nV r.1981 prišlo k výmene predsedu oddielu OB a na tento post nastúpila Soňa Váliková-Galádová. Zakrátko nastala ďalšia funkcionárska výmena na čele oddielu a v r.1982 sa stal predsedom oddielu OB Dušan Formanko, ktorý je v tomto činný dodnes. ALT\r\n\r\nBohatá je činnosť oddielu i v hnutí orientačného behu, kde máme na všetkých úrovniach desiatky profesionálnych rozhodcov, organizátorov, trénerov, kartografov a funkcionárov. Z našich radov vyšli reprezentanti troch republík (ČSSR, ČSFR a SR), ako boli a sú Pavol Brunovský, Jaroslav Jašek, Juraj Petrinec, Miroslav Stržínek, Ľudovít Šmelík, Mikuláš Šabo, Oľga Vigašová, Hana Bajtošová. Tituly a medailové umiestnenia na majstrovských i rebríčkových súťažiach získavali v minulosti i v súčasnosti aj ďalší naši športovci: J. Petrinec, K. Hrabinský, P. Sláma ml., M. Petrinec, J. Šmelík, M. Šabo, P. Sláma st., Ľ. Šmelík, I. Prieložná, A. Kľučková, Z. Briedová, H. Bajtošová, Z. Kátlovská, I. Kumová a mnoho ďalších.\r\n\r\nOddiel aktívne a kvalitne usporiadal preteky na úrovni Majstrovstiev Slovenska:\r\nr.1982 dlhá trať (mapa Cerová dráha)\r\nr.1991 dlhá trať (mapa Čerťaž)\r\nr.1994 klasická trať a štafety (mapa Pukanec – Breziny)\r\nr.1996 krátka trať (mapa Snežienka)\r\n\r\nALT a celoštátne rebríčkové súťaže:\r\nr.1981 Slovenský rebríček štafiet (mapa Zrkadlový háj)\r\nr.1984 Slovenský rebríček jednotlivcov (mapa Tri duby)\r\nr.1988 Slovenský rebríček štafiet (mapa Červený kameň)\r\nr.1990 Slovenský rebríček jednotlivcov (mapa Lindavský les)\r\nr.1997 Slovenský rebríček jednotlivcov a štafiet (mapa Snežienka)\r\nr.2001 Slovenský rebríček jednotlivcov (mapa Marianka)\r\nr.2003 Slovenský rebríček jednotlivcov (mapa Kučišdorf)\r\nr.2005 Slovenský rebríček jednotlivcov (mapa Driny – Jahodník)\r\n\r\nAj po roku 2000 patrí náš oddiel medzi najväčšie na Slovensku a dokáže zabezpečiť svojim členom kvalitné podmienky na tréning a rozvoj výkonnostného i vrcholového orientačného behu.\r\n\r\n<a href="/site_media/upload/ob/historia/big/ob4.jpg"><img src="/site_media/upload/ob/historia/small/ob4.jpg" alt="" class="pic-left" /></a>\r\n\r\nPravidelne dosahujeme veľmi dobré výsledky v Slovenskom rebríčku jednotlivcov, aj v celkovom hodnotení klubových družstiev, kde sme sa umiestnili:\r\nV roku 2001 na 3. mieste\r\nV roku 2003 na 2. mieste\r\nV roku 2004 na 2. mieste\r\nV roku 2005 na 2. mieste\r\nV roku 2006 na 2. mieste\r\n\r\nV posledných 5 rokoch dosahujú výborné výsledky hlavne mladí pretekári, H. Bajtošová, Martin Mazúr, J. Priesol, ktorí reprezentujú nielen náš oddiel, ale ako členovia dorasteneckej a juniorskej reprezentácie aj Slovenskú republiku.\r\nNajvýraznejšie výsledky dosahuje v súčasnosti Martin Mazúr, ktorý bol v roku 2003 členom bronzovej štafety na Majstrovstvách Európy dorastencov v Pezinku a v roku 2004 členom zlatej štafety na Majstrovstvách Európy dorastencov v Salzburgu. V tom istom roku získal bronzovú medailu na skrátenej trati na Majstrovstvách sveta školskej mládeže v Belgicku.\r\n\r\nVeľmi dobré výsledky dosahujú členovia nášho oddielu aj v súťažiach v orientačnej cyklistike na horských bicykloch. V roku 2004 sa stali majstrami Slovenska Martin Mazúr v kategórii M-18 a Mikuláš Šabo v hlavnej kategórii M 19-. Mikuláš Šabo sa zároveň v rokoch 2005 a 2006 stal celkovým víťazom Slovenského pohára v orientačnej cyklistike. V roku 2004 reprezentoval Slovenskú republiku na Majstrovstvách sveta v Austrálii a v roku 2005 bol členom slovenského družstva, ktoré v pretekoch štafiet na Majstrovstvách sveta v orientačnej cyklistike v B. Bystrici skončilo na 8. mieste.\r\nNajväčší úspech v histórii Slovenska dosiahla v orientačnej cyklistike Hana Bajtošová, ktorá na Majstrovstvách sveta v orientačnej cyklistike v roku 2005 skončila v pretekoch na klasickej trati (long) na 6. mieste, v pretekoch na skrátenej trati (middle) na 8. mieste, a bola členkou slovenského družstva, ktoré v pretekoch štafiet skončilo na 8. mieste. Zároveň v roku 2005 skončila v celkovom hodnotení Slovenského pohára v orientačnej cyklistike na 2. mieste.\r\n\r\nV roku 2006 oslávil náš oddiel 40. výročie. 	2007-09-22 22:07:12.174038+01	2007-09-22 22:07:12.174075+01
5	Výbor oddielu	vybor	1	| Predseda: | "Dušan Formanko":mailto:formanko@t-zones.sk  |\r\n| Podpredseda: | "Milan Petrinec":mailto:tatraprojekt@nextra.sk |\r\n| Tajomník: | "František Priesol":mailto:frantisek.priesol@gmail.com |\r\n| Členovia výboru: | "Milan Mazúr":mailto:mazurm@zoznam.sk, "Iva Kumová":mailto:kumova@centrum.sk |\r\n| Hospodár: | Ľudmila Formanková (nie je členom výboru) |	2007-09-22 22:08:30.515146+01	2007-09-22 22:08:30.515183+01
6	Mapy	mapy	1	table(standard).\r\n|_. Názov mapy:  | Mierka:  | Rok vydania:  | Plocha km2:  | Mapoval(i): |\r\n| Ostredky-Ružinov | 1:5 000 | 2006 | 1,1 | M. Petrinec |\r\n| Driny-Jahodník | 1:10 000 | 2005 | 5,0 | M. Spišiak, M. Petrinec |\r\n| Ostredky | 1:4 000 | 2004 | 0,2 | M. Lago, M. Petrinec |\r\n| Marianka | 1:15 000 | 2000 | 10,5 | M. Petrinec |\r\n| Stupavský park | 1:5 000 | 2000 | 1,0 | M. Petrinec |\r\n| Kopec | 1:5 000 | 2000 | 1,0 | M. Petrinec |\r\n| Snežienka | 1:15 000 | 1996 | 6,0 | M. Petrinec |\r\n| Pukanec - Breziny | 1:15 000 | 1994 | 10,0 | M. Petrinec, P. Krišpinský, R. Sučík |\r\n| Devínska kobyla | 1:15 000 | 1992 | 9,0 | A. Kniebugel |\r\n| Lindavský les | 1:15 000 | 1990 | 7,0 | M. Petrinec |\r\n| Červený kameň | 1:15 000 | 1987 | 4,5 | M. Petrinec |\r\n| Stánisko | 1:15 000 | 1985 | 10,5 | M. Petrinec |\r\n| Kačín | 1:15 000 | 1985 | 8,0 | P. Barták, E. Onrejička, M. Petrinec |\r\n| Tri duby | 1:15 000 | 1984 | 11,0 | J. Petrinec, M. Petrinec |\r\n| Cerová dráha | 1:15 000 | 1983 | 6,5 | M. Petrinec |\r\n| Cerová dráha | 1:15 000 | 1982 | 6,5 | M. Petrinec |\r\n| Báthory | 1:15 000 | 1981 | 8,0 | P. Krišpinský, M. Šťastný |\r\n| Zrkadlový háj | 1:10 000 | 1981 | 5,5 | P. Krišpinský |\r\n| Orientačný pochod VI. ročník | 1:20 000 | 1979 | 8,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod V. ročník | 1:20 000 | 1978 | 14,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod IV. ročník | 1:20 000 | 1977 | 7,5 | F. Gallo, P. Krišpinský |\r\n| Húštiny | 1:20 000 | 1977 | 5,0 | P. Krišpinský, Š. Šujan, P. Sláma st. |\r\n| Chlmec | 1:20 000 | 1977 | 9,5 | P. Krišpinský, F. Gallo, M. Šťastný |\r\n| Orientačný pochod III. ročník | 1:20 000 | 1976 | 5,0 | F. Gallo |\r\n| Lindav | 1:20 000 | 1976 | 11,5 | P. Krišpinský, M. Šeliga |\r\n| M- SSR SZM | 1:20 000 | 1976 | 11,5 | P. Krišpinský, M. Šeliga |\r\n| Kamzík | 1:16 667 | 1975 | 5,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod II. ročník | 1:20 000 | 1975 | 5,0 | F. Gallo, P. Krišpinský |\r\n| Pekný les | 1:20 000 | 1975 | 6,0 | F. Gallo, P. Krišpinský |\r\n| Táľky | 1:20 000 | 1974 | 9,0 | F. Gallo, P. Hrdlovič, Krišpinský, Šeliga |\r\n| Panský les | 1:20 000 | 1974 | 6,0 | P. Sláma st., Š. Šujan |\r\n| Kozlisko | 1:20 000 | 1971 | 15,0 | Novotný |\r\n| Ravnica | 1:20 000 | 1971 | 11,0 | kolektív RBA |\r\n| Zudrok | 1:20 000 | 1970 | 7,5 | Ľ. Šmelík |\r\n| Kamzík | 1:16 666 | 1970 | 5,0 | P. Samuel |	2007-09-22 22:14:53.519376+01	2007-09-22 22:54:00.678844+01
7	Úvod		6	Oddiel cyklistiky na oslave 70. výročia založenia TJ Rapid:\r\n\r\n<img src="/site_media/upload/cyklo/70.jpg" alt="" class="pic" />	2007-10-05 00:44:56.834336+01	2007-10-05 00:44:56.83442+01
8	Úvod		9	V Bratislave pôsobí oddiel modernej gymnastiky (MG) TJ Rapid Bratislava už vyše dvadsať rokov. Svoju činnosť vykonáva vo Vrakuni a v Petržalke. O členky oddielu sa stará osem kvalifikovaných tréneriek a rozhodkýň, ktoré sú registrované v Slovenskom zväze modernej gymnastiky.\r\n\r\n<img src="/site_media/upload/gymnastika/oddiel_s.jpg" alt="" class="pic-right" />\r\n\r\nDievčatá, ktoré sú členkami oddielu, na tréningoch získavajú základy pohybovej výchovy, akrobacie, klasického tanca a cvičenia s gymnastickým náčiním.\r\n\r\nOrganizujeme letné sústredenia, kde nacvičujeme nové voľné zostavy a tanečné choreografie.\r\n\r\nV športových súťažiach MG na Slovensku náš oddiel dosahuje veľmi dobré výsledky najmä v kategórii spoločných skladieb.\r\n\r\nZáujemkyne o tento šport vo veku 5 - 9 rokov srdečne pozývame na naše tréningy:\r\n\r\n* Vrakuňa: telocvičňa ZŠ Železničná 14 (pondelok a streda 16.00 - 18.00)\r\n* Petržalka: športová hala Pengym na Znievskej ulici, oproti Draždiaku (utorok a piatok 16.30 - 18.30)\r\n\r\nBližšie informácie o tomto športe aj o našom oddieli vám poskytneme na tel. č. 02/55571448.\r\n	2007-10-05 00:46:15.497281+01	2007-10-05 00:46:15.497363+01
10	Úvod		7	Oddiel hádzanej v TJ Rapid Bratislava vznikol v roku 1968 a venoval sa všetkým vekovým kategóriám. Žiaci, dorastenci, i muži súťažili v celoštátnych – Československých i Slovenských súťažiach.\r\nV roku 1978 sa na Majstrovstvách ČSSR umiestnili žiaci na 3. mieste a na Majstrovstvách SSR na 2. mieste.\r\n\r\nDorastenci a mladší žiaci boli dlhodobí účastníci I. Školskej ligy v rokoch 1972 – 1987.\r\nDružstvo mužov bojovalo v II. lige ČSSR a v roku 1985 sa umiestnilo na 2. mieste.\r\nZ našich radov vyšli hráči, ktorí úspešne reprezentovali ČSSR ako Jaroslav Holeš, Igor Krba a reprezentant SR Michal Baran.\r\n\r\nMôžeme sa pochváliť aj výbornými prvoligovými hráčmi – Dušan Orosz, Pavol Vávik, Marián Kubovič, Jozef Hamala, Dušan Jeleník.\r\n\r\nV súčasnosti Oddiel hádzanej pracuje a súťaží v kategóriách starší žiaci, mladší žiaci a prípravná kategória.\r\n\r\nPôsobnosť a tréningy hádzanárov sú na ZŠ Nevädzová 2, 821 01 Bratislava.\r\n\r\nPondelok: 15:00 – 17:00 mladší žiaci, prípravka\r\nUtorok: 15:00 – 17:00 starší žiaci\r\nStreda: 15:00 – 17:00 mladší žiaci, prípravka\r\nŠtvrtok: 15:00 – 17:00 starší žiaci\r\nPiatok: 14:00 – 16:00 prípravka\r\n\r\nVšetky informácie o činnosti Oddielu hádzanej, tréningoch, súťažiach a športovom dianí v hádzanej dostanete u predsedu oddielu pána Milana Bujalku na tel. č. 02 / 43 42 35 52\r\n\r\nOddiel hádzanej na oslave 70. výročia založenia TJ Rapid:\r\n\r\n<img src="/site_media/upload/hadzana/70.jpg" alt="" class="pic" />	2007-10-05 00:47:31.810518+01	2007-10-05 00:47:31.810601+01
11	Karate		8	Oddiel karate na oslave 70. výročia založenia TJ Rapid:\r\n\r\n<img src="/site_media/upload/karate/70.jpg" alt="" class="pic" />	2007-10-05 00:47:53.314134+01	2007-10-05 00:47:53.314217+01
12	Úvod		10	Oddiel turistiky patrí medzi najstaršie športové činnosti v našej TJ, nadväzuje na tradície starých Prievozčanov – "Feribákov" v KČSTL, Naturfreunde a trampských osád.\r\n\r\nOrganizovaná turistika u nás sa uskutočňuje kolektívne, pod zodpovedným vedením cvičiteľov v podobe kondičných túr do prírody v každom ročnom období, aby sa tak upevňovalo zdravie a vôľové vlastnosti členov. Na túto činnosť nadväzuje výkonnostná turistika po línii zápočtových ciest, presunov, odznakov rôznych oblastí, ... Nami organizovaná turistika je vhodná pre všetky vekové kategórie od mládeže až po staršie ročníky, a to aj ako doplnkový šport.\r\n\r\nKolektivizmus v turistike nebráni rozvoju osobnosti a individuálnych schopností členov, ale odstraňuje zbytočnú rivalitu, ktorá u niektorých športov vedie až k používaniu nečestných spôsobov súperenia.\r\nŠtvrťročne vydávame zoznam akcií. Program túr býva zverejnený i v časopise "Kam v Bratislave" (mesačník vydávaný BIS-kou). Vítaní sú záujemcovia najmä zo spádovej oblasti Prievoz – Ružinov, ale i z celej Bratislavy.\r\n\r\nZáujemcovia o tento šport sa môžu informovať priamo na sekretariáte TJ RAPID, alebo u predsedu Oddielu turistiky, pána Jozefa Kubíčka, na tel. č. 02 / 43 33 21 14.	2007-10-05 00:48:17.744839+01	2007-10-05 00:48:17.744918+01
9	Fotografie	fotografie	9	<img src="/site_media/upload/gymnastika/ph1.jpg" alt="" class="pic-left" style="clear: both" />\r\n<img src="/site_media/upload/gymnastika/ph2.jpg" alt="" class="pic-right" style="clear: both" />\r\n<img src="/site_media/upload/gymnastika/ph3.jpg" alt="" class="pic-left" style="clear: both" />\r\n<img src="/site_media/upload/gymnastika/ph4.jpg" alt="" class="pic-right" style="clear: both" />\r\n<img src="/site_media/upload/gymnastika/ph5.jpg" alt="" class="pic-left" style="clear: both" />\r\n<div style="clear: both"></div>	2007-10-05 00:46:45.916873+01	2007-10-05 00:49:08.434897+01
13	About	about	5	History of Foot-orienteering Club TJ Rapid Bratislava\r\n\r\nALT Our club is one of the first clubs with the foot-orienteering that had been found in former Czechoslovakia. A group of volunteers and enthusiasts for this kind of sport from SLAVIA SVST and LOKOMOTIVA BRATISLAVA has decided to find out better conditions for development of their work and in 1966 they established a club of foot-orienteering near TJ RAPID BRATISLAVA. The first head was Ing. Mojmír Šeliga. The results they have achieved in that era are showing that there were conditions for training altogether with top-performance sport.\r\n\r\nFor illustration:\r\n1966 Slovak Orienteering Championship of Czechoslovakia – Ľ. Šmelík 3.place\r\n1968 Slovak Orienteering Championship – Ľ. Šmelík 1.place, O.Vigašová 1.place\r\n1969 Slovak Orienteering Championship - relay (Ľ. Šmelík, L. Hýbal, J.Jašek)1.place\r\n1970 Slovak Cup – P. Sláma 1. place, Ľ. Šmelík 2.miesto\r\n1970 Czechoslovakia Team Cup – TJ Rapid 6.place\r\n1971 Slovak Cup – Ľ. Šmelík 1.place, P. Sláma 2.place\r\n\r\nFoot-orienteering runners TJ Rapid Bratislava were successful not only in sport and efficiency, but they were part of and also pioneered in other fields of orienteering. In 1968 they initiated the establishment of SLOVAK FOOT-ORIENTEERING FEDERATION and Mojmír Šeliga - ‘rapidian’ became the head of the federation. The organization has not stayed in back. The club organized sport-stay in Sweden - ‘Mecca of foot-orienteering’. The idea of international several-day event became true and in 1971 our club prepared the 1st Grand Prix Slovakia (GPS) on maps: Zurdok, Ravnica and Kamzík. In 1972, we organized also 3rd GPS on maps: Pekný les, Vetrov plac and Kamzík.\r\n\r\nALT As a next traditional event was the 1st Spring Suitcase, which began in 1973 and have been organised every year till nowadays. We have also organized several times the highest rating national competition – Czechoslovak Orienteering Championship in 1974 – classic and relay, in 1977 – long distance (map Červený kameň), in 1983 – long distance (map Lažetky 1,2,3), in 1985 – classical distance and relay (Maps Stánisko and Kačín).\r\n\r\nFrom 1976, Viktor Vávra was leading the club of orienteering. During his head position, a new wave of talented children flew into the club and many of them stayed active in orienteering till nowadays. For example: A. Autrata, brothers Petrincovci, A. Kĺučková, E.Pukalovičová, sisters Lukáškové, P. Sláma Jnr., …\r\n\r\nIn 1981, Soňa Váliková-Galádová replaced the head of club, but in a short time next exchange followed. In 1982 Dušan Formanko was elected onto the leading position and he has been in this function till now. ALT\r\n\r\nThe functioning of our club is really plentiful. We have many of professional referees, organizers, trainers, professionals in cartography and officers. Many runners grew up and are still growing up to representation of one of three republics (Czechoslovak socialist, Czechoslovak federal and Slovak) in our club: Pavol Brunovský, Jaroslav Jašek, Juraj Petrinec, Miroslav Stržínek, Ľudovít Šmelík, Mikuláš Šabo, Oľga Vigašová, Hana Bajtošová. The titles and medallic positions of Championships and Cups have reached also other sportswomen/men: J. Petrinec, L. Hrabinský, P. Sláma Jnr., M. Petrinec, J. Šmelík, M. Šabo, P. Sláma Snr., Ľ. Šmelík, I. Prieložná, A. Kľučková, Z. Briedová, H. Bajtošová, Z. Kátlovská, I. Kumová and many others.\r\n\r\nThe club has organized Slovak Championships actively and in a good quality:\r\n1982 Long distance (map Cerová dráha)\r\n1991 Long distance (map Čerťaž)\r\n1994 classical distance a relay (map Pukanec - Breziny)\r\n1996 short distance (map Snežienka)\r\n\r\nALT ... and Slovak Cups:\r\n1984 Slovak Cup - Individuals (map Tri duby)\r\n1988 Slovak Cup - relay (map Červený kameň)\r\n1990 Slovak Cup - Individuals (map Lindavský les)\r\n1997 Slovak Cup - Individuals and relays (map Snežienka)\r\n2000 Slovak Cup - Individuals (map Marianka)\r\n2001 Slovak Cup - Individuals (map Marianka)\r\n\r\nNowadays, we are the biggest club in Slovakia in the number of members – 65, although, we are still able to provide good quality conditions for training and improvement of top-performance foot-orienteering.\r\n	2007-10-05 00:59:07.328649+01	2007-10-05 01:14:34.688824+01
15	Maps	maps	5	Our club is publisher and owner of maps for foot-O:\r\n\r\ntable(standard).\r\n|_. Name:  | Scale:  | Year of printing:  | Area km2:  | Maped by: |\r\n| Ostredky-Ružinov | 1:5 000 | 2006 | 1,1 | M. Petrinec |\r\n| Driny-Jahodník | 1:10 000 | 2005 | 5,0 | M. Spišiak, M. Petrinec |\r\n| Ostredky | 1:4 000 | 2004 | 0,2 | M. Lago, M. Petrinec |\r\n| Marianka | 1:15 000 | 2000 | 10,5 | M. Petrinec |\r\n| Stupavský park | 1:5 000 | 2000 | 1,0 | M. Petrinec |\r\n| Kopec | 1:5 000 | 2000 | 1,0 | M. Petrinec |\r\n| Snežienka | 1:15 000 | 1996 | 6,0 | M. Petrinec |\r\n| Pukanec - Breziny | 1:15 000 | 1994 | 10,0 | M. Petrinec, P. Krišpinský, R. Sučík |\r\n| Devínska kobyla | 1:15 000 | 1992 | 9,0 | A. Kniebugel |\r\n| Lindavský les | 1:15 000 | 1990 | 7,0 | M. Petrinec |\r\n| Červený kameň | 1:15 000 | 1987 | 4,5 | M. Petrinec |\r\n| Stánisko | 1:15 000 | 1985 | 10,5 | M. Petrinec |\r\n| Kačín | 1:15 000 | 1985 | 8,0 | P. Barták, E. Onrejička, M. Petrinec |\r\n| Tri duby | 1:15 000 | 1984 | 11,0 | J. Petrinec, M. Petrinec |\r\n| Cerová dráha | 1:15 000 | 1983 | 6,5 | M. Petrinec |\r\n| Cerová dráha | 1:15 000 | 1982 | 6,5 | M. Petrinec |\r\n| Báthory | 1:15 000 | 1981 | 8,0 | P. Krišpinský, M. Šťastný |\r\n| Zrkadlový háj | 1:10 000 | 1981 | 5,5 | P. Krišpinský |\r\n| Orientačný pochod VI. ročník | 1:20 000 | 1979 | 8,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod V. ročník | 1:20 000 | 1978 | 14,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod IV. ročník | 1:20 000 | 1977 | 7,5 | F. Gallo, P. Krišpinský |\r\n| Húštiny | 1:20 000 | 1977 | 5,0 | P. Krišpinský, Š. Šujan, P. Sláma st. |\r\n| Chlmec | 1:20 000 | 1977 | 9,5 | P. Krišpinský, F. Gallo, M. Šťastný |\r\n| Orientačný pochod III. ročník | 1:20 000 | 1976 | 5,0 | F. Gallo |\r\n| Lindav | 1:20 000 | 1976 | 11,5 | P. Krišpinský, M. Šeliga |\r\n| M- SSR SZM | 1:20 000 | 1976 | 11,5 | P. Krišpinský, M. Šeliga |\r\n| Kamzík | 1:16 667 | 1975 | 5,0 | P. Krišpinský, F. Gallo |\r\n| Orientačný pochod II. ročník | 1:20 000 | 1975 | 5,0 | F. Gallo, P. Krišpinský |\r\n| Pekný les | 1:20 000 | 1975 | 6,0 | F. Gallo, P. Krišpinský |\r\n| Táľky | 1:20 000 | 1974 | 9,0 | F. Gallo, P. Hrdlovič, Krišpinský, Šeliga |\r\n| Panský les | 1:20 000 | 1974 | 6,0 | P. Sláma st., Š. Šujan |\r\n| Kozlisko | 1:20 000 | 1971 | 15,0 | Novotný |\r\n| Ravnica | 1:20 000 | 1971 | 11,0 | kolektív RBA |\r\n| Zudrok | 1:20 000 | 1970 | 7,5 | Ľ. Šmelík |\r\n| Kamzík | 1:16 666 | 1970 | 5,0 | P. Samuel |\r\n\r\nAdministrator of printed maps is Dušan Formanko.	2007-10-05 01:28:43.114149+01	2007-10-05 01:31:12.213527+01
14	Committee	committee	5	| Chairman: | "Dušan Formanko":mailto:formanko@t-zones.sk  |\r\n| Deputy chairman: | "Milan Petrinec":mailto:tatraprojekt@nextra.sk |\r\n| Secretary: | "František Priesol":mailto:frantisek.priesol@gmail.com |\r\n| Členovia výboru: | "Milan Mazúr":mailto:mazurm@zoznam.sk, "Iva Kumová":mailto:kumova@centrum.sk |\r\n| Treasurer: | Ľudmila Formanková (nie je členom výboru) |	2007-10-05 01:15:52.877146+01	2007-10-05 01:32:34.534209+01
\.


--
-- Data for Name: ob_competition; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY ob_competition (id, title, name, start_date, end_date, "location", specification, results, photos) FROM stdin;
1	Milá míľa (cross)	mila-mila-2007	2007-05-13	\N	Bratislava	mila-mila-2007.rtf		
2	Jesenná cena Rapidu	jesenna-cena-rapidu-2007	2007-10-07	\N	Bratislava	jesenna-cena-rapidu-2007.doc	jesenna-cena-rapidu-2007.doc	http://www.tjrapid.sk/
\.


--
-- Data for Name: ob_member; Type: TABLE DATA; Schema: public; Owner: tjrapid
--

COPY ob_member (id, first_name, surname, category, email) FROM stdin;
1	Iva	Kumová	W45-	kumova@centrum.sk
4	Jakub	Schenk	M-10R	
5	Túró	Tomáš	M-10R	
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_message_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_flatpage_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_flatpage
    ADD CONSTRAINT django_flatpage_pkey PRIMARY KEY (id);


--
-- Name: django_flatpage_sites_flatpage_id_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_flatpage_id_key UNIQUE (flatpage_id, site_id);


--
-- Name: django_flatpage_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: main_category_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY main_category
    ADD CONSTRAINT main_category_pkey PRIMARY KEY (id);


--
-- Name: main_language_code_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY main_language
    ADD CONSTRAINT main_language_code_key UNIQUE (code);


--
-- Name: main_language_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY main_language
    ADD CONSTRAINT main_language_pkey PRIMARY KEY (id);


--
-- Name: main_page_name_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY main_page
    ADD CONSTRAINT main_page_name_key UNIQUE (name, category_id);


--
-- Name: main_page_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY main_page
    ADD CONSTRAINT main_page_pkey PRIMARY KEY (id);


--
-- Name: ob_competition_name_key; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY ob_competition
    ADD CONSTRAINT ob_competition_name_key UNIQUE (name);


--
-- Name: ob_competition_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY ob_competition
    ADD CONSTRAINT ob_competition_pkey PRIMARY KEY (id);


--
-- Name: ob_member_pkey; Type: CONSTRAINT; Schema: public; Owner: tjrapid; Tablespace: 
--

ALTER TABLE ONLY ob_member
    ADD CONSTRAINT ob_member_pkey PRIMARY KEY (id);


--
-- Name: auth_message_user_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX auth_message_user_id ON auth_message USING btree (user_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_flatpage_url; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX django_flatpage_url ON django_flatpage USING btree (url);


--
-- Name: main_category_language_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX main_category_language_id ON main_category USING btree (language_id);


--
-- Name: main_category_name; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX main_category_name ON main_category USING btree (name);


--
-- Name: main_page_category_id; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX main_page_category_id ON main_page USING btree (category_id);


--
-- Name: main_page_name; Type: INDEX; Schema: public; Owner: tjrapid; Tablespace: 
--

CREATE INDEX main_page_name ON main_page USING btree (name);


--
-- Name: auth_group_permissions_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_flatpage_sites_flatpage_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_flatpage_id_fkey FOREIGN KEY (flatpage_id) REFERENCES django_flatpage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_flatpage_sites_site_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY django_flatpage_sites
    ADD CONSTRAINT django_flatpage_sites_site_id_fkey FOREIGN KEY (site_id) REFERENCES django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: language_id_refs_id_224a59; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY main_category
    ADD CONSTRAINT language_id_refs_id_224a59 FOREIGN KEY (language_id) REFERENCES main_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: main_page_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY main_page
    ADD CONSTRAINT main_page_category_id_fkey FOREIGN KEY (category_id) REFERENCES main_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_650f49a6; Type: FK CONSTRAINT; Schema: public; Owner: tjrapid
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT user_id_refs_id_650f49a6 FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

