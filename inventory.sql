PGDMP      #    ;            
    {         	   inventory #   14.9 (Ubuntu 14.9-0ubuntu0.22.04.1) #   14.9 (Ubuntu 14.9-0ubuntu0.22.04.1)     %           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            &           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            '           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            (           1262    96978 	   inventory    DATABASE     ^   CREATE DATABASE inventory WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';
    DROP DATABASE inventory;
                aliepratama    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false            )           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    3            �            1259    96990 
   categories    TABLE     o   CREATE TABLE public.categories (
    id integer NOT NULL,
    category_name character varying(100) NOT NULL
);
    DROP TABLE public.categories;
       public         heap    odoo15    false    3            �            1259    96989    categories_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public          odoo15    false    3    212            *           0    0    categories_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;
          public          odoo15    false    211            �            1259    96980    products    TABLE     Y  CREATE TABLE public.products (
    id integer NOT NULL,
    product_name character varying(100) NOT NULL,
    stock numeric NOT NULL,
    price numeric NOT NULL,
    image_link character varying(255),
    description character varying(255),
    category_id integer NOT NULL,
    CONSTRAINT products_stock_check CHECK ((stock > (0)::numeric))
);
    DROP TABLE public.products;
       public         heap    odoo15    false    3            �            1259    96979    products_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.products_id_seq;
       public          odoo15    false    210    3            +           0    0    products_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;
          public          odoo15    false    209            �           2604    96993    categories id    DEFAULT     n   ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);
 <   ALTER TABLE public.categories ALTER COLUMN id DROP DEFAULT;
       public          odoo15    false    212    211    212            �           2604    96983    products id    DEFAULT     j   ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);
 :   ALTER TABLE public.products ALTER COLUMN id DROP DEFAULT;
       public          odoo15    false    210    209    210            "          0    96990 
   categories 
   TABLE DATA           7   COPY public.categories (id, category_name) FROM stdin;
    public          odoo15    false    212   �                  0    96980    products 
   TABLE DATA           h   COPY public.products (id, product_name, stock, price, image_link, description, category_id) FROM stdin;
    public          odoo15    false    210   .       ,           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 6, true);
          public          odoo15    false    211            -           0    0    products_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.products_id_seq', 13, true);
          public          odoo15    false    209            �           2606    96995    categories categories_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            odoo15    false    212            �           2606    96988    products products_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            odoo15    false    210            �           2606    96996    products products_categories    FK CONSTRAINT     �   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_categories FOREIGN KEY (category_id) REFERENCES public.categories(id) ON UPDATE CASCADE;
 F   ALTER TABLE ONLY public.products DROP CONSTRAINT products_categories;
       public          odoo15    false    210    3218    212            "   )   x^3����+�M��2��M�N���8R����b�=... ��
?             x^����� � �     