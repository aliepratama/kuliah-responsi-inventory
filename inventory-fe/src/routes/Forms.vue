<script>
import axios from "axios";

export default {
    props: ['id'],
    data(){
        return {
            categories: null,
            nama_produk: null,
            stok: null,
            harga: null,
            deskripsi: null,
            kategori: null,
        }
    },
    computed: {
        isEdit(){
            return Boolean(this.id)
        }
    },
    mounted(){
        this.fetchData()
    },
    methods: {
        submitProduct(){
            this.isEdit ? this.editProduct(this.id) : this.createProduct();
            this.$router.push('/products');
        },
        fetchProduct(id){
            axios.get(`http://127.0.0.1:5000/products/${id}`)
            .then(res => {
                let data = res.data.data;
                this.nama_produk = data.nama_produk;
                this.stok = data.stok;
                this.harga = data.harga;
                this.deskripsi = data.deskripsi;
                this.kategori = data.kategori;
            })
        },
        fetchData(){
            axios.get('http://127.0.0.1:5000/categories/lists')
            .then(res => {
                this.categories = res.data.data
            }).then(() => {
                if(this.isEdit){
                    this.fetchProduct(this.id);
                }
            })
        },
        createProduct(){
            axios.post('http://127.0.0.1:5000/products/lists', {
                nama_produk: this.nama_produk,
                stok: this.stok,
                harga: this.harga,
                deskripsi: this.deskripsi,
                kategori: this.kategori,
            }, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(res => alert(res.data.message))
        },
        editProduct(id){
            axios.patch(`http://127.0.0.1:5000/products/${id}`, {
                nama_produk: this.nama_produk,
                stok: this.stok,
                harga: this.harga,
                deskripsi: this.deskripsi,
                kategori: this.kategori,
            }, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }).then(res => alert(res.data.message))
        },
    }
}
</script>
<template>
    <div>
        <div>
            <div class="max-w-4xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
                <!-- Card -->
                <div class="bg-white rounded-xl shadow p-4 sm:p-7 dark:bg-slate-900">
                    <form>
                    <!-- Section -->
                        <div class="grid sm:grid-cols-12 gap-2 sm:gap-4 py-8 first:pt-0 last:pb-0 border-t first:border-transparent border-gray-200 dark:border-gray-700 dark:first:border-transparent">
                            <div class="flex items-center sm:col-span-12">
                                <router-link to="/products" type="button" class="py-2 px-3 flex justify-center items-center h-[2.875rem] w-[2.875rem] text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="white" stroke="currentColor" height="1em" viewBox="0 0 448 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/></svg>
                                </router-link>
                                <h2 class="text-lg font-semibold text-gray-800 dark:text-gray-200 ml-4">
                                    Detail Produk
                                </h2>
                            </div>

                            <div class="sm:col-span-3">
                                <label for="nama_produk" class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                    Nama Produk
                                </label>
                            </div>
                        <!-- End Col -->

                            <div class="sm:col-span-9">
                                <input
                                    id="nama_produk"
                                    type="text" 
                                    class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="Tambahkan nama produk"
                                    v-model="nama_produk">
                            </div>
                            <!-- End Col -->

                            <div class="sm:col-span-3">
                                <label for="stok" class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                    Stok
                                </label>
                            </div>
                        <!-- End Col -->

                            <div class="sm:col-span-3">
                                <input 
                                    id="stok" 
                                    type="text" 
                                    class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="Tambahkan stok"
                                    v-model="stok">
                            </div>
                            <!-- End Col -->

                            <div class="sm:col-span-3">
                                <label for="harga" class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                    Harga
                                </label>
                            </div>
                        <!-- End Col -->

                            <div class="sm:col-span-3">
                                <input 
                                id="harga" 
                                type="text" 
                                class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" 
                                placeholder="Tambahkan harga"
                                v-model="harga">
                            </div>
                            <!-- End Col -->

                            <div class="sm:col-span-3">
                                <label for="textarea-label" class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                    Deskripsi
                                </label>
                            </div>
                        <!-- End Col -->
                            <div class="sm:col-span-9">
                                <textarea 
                                id="textarea-label" 
                                class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" rows="3" 
                                placeholder="Tambahkan deskripsi..."
                                v-model="deskripsi"></textarea>
                            </div>
                            <!-- End Col -->
                            <div class="sm:col-span-3">
                                <label for="kategori" class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                    Kategori
                                </label>
                            </div>
                        <!-- End Col -->
                            <div class="sm:col-span-9">
                                <select id="kategori" v-model="kategori" class="py-2 px-8 pe-12 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600 sm:p-4">
                                    <option selected v-if="!isEdit">Pilih kategori</option>
                                    <option v-for="category in categories" :key="category.id" :value="category.id" :selected="category.id == kategori">{{ category.nama_kategori }}</option>
                                </select>
                            </div>
                            <!-- End Col -->
                        </div>
                        <div class="sm:col-span-12">
                            <button 
                                type="button" 
                                @click="submitProduct()"
                                class="w-full py-3 px-4 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                                {{isEdit ? 'Edit': 'Tambah'}} Produk
                            </button>
                        </div>
                    </form>
                </div>
                <!-- End Card -->
                </div>
        </div>
    </div>
</template>