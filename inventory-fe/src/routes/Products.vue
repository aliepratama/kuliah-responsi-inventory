<script>
import axios from 'axios';
export default {
    data(){
        return {
            datalists: [],
        }
    },
    mounted(){
        this.fetchData();
    },
    methods: {
        fetchData(){
            axios.get('http://127.0.0.1:5000/products/lists')
            .then(res => {
                this.datalists = res.data.data;
            });
        },
        deleteData(id){
            axios.delete(`http://127.0.0.1:5000/products/${id}`)
            .then(res => {
                this.fetchData();
            });
        },
    },
}
</script>
<template>
    <div class="divide-gray-200 dark:divide-gray-700 min-w-full px-16">
        <div class="flex justify-between py-10">
            <div>
                <h2 class="font-bold text-lg">Daftar Produk</h2>
            </div>
            <div>
                <router-link to="/form" type="button" class="px-4 py-2 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:bg-blue-100 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:bg-blue-800/30 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                    Tambah Produk
                </router-link>
            </div>
        </div>
        <div>
            <div class="flex flex-col">
                <div class="-m-1.5 overflow-x-auto">
                    <div class="p-1.5 min-w-full inline-block align-middle">
                        <div class="overflow-hidden">
                            <table v-if="datalists.length > 0" class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead>
                                    <tr>
                                        <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Nama Produk</th>
                                        <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Stok</th>
                                        <th scope="col" class="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase">Harga</th>
                                        <th scope="col" class="px-6 py-3 text-end text-xs font-medium text-gray-500 uppercase">Aksi</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="data in datalists" :key="data.id" class="odd:bg-white even:bg-gray-100 hover:bg-gray-100 dark:odd:bg-gray-800 dark:even:bg-gray-700 dark:hover:bg-gray-700">
                                        <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800 dark:text-gray-200">{{ data.nama_produk }}</td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200">{{ data.stok }}</td>
                                        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-800 dark:text-gray-200">{{ data.harga }}</td>
                                        <td class="flex px-6 py-4 whitespace-nowrap text-end text-sm font-medium justify-between">
                                            <div class="flex items-center">
                                                <router-link :to="{ name: 'Details', params: { id: data.id }}" class="inline-flex ml-2 items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="#1e40af" height="1em" viewBox="0 0 512 512"><path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336h24V272H216c-13.3 0-24-10.7-24-24s10.7-24 24-24h48c13.3 0 24 10.7 24 24v88h8c13.3 0 24 10.7 24 24s-10.7 24-24 24H216c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"/></svg>
                                                    Lihat Detail
                                                </router-link>
                                            </div>
                                            <div class="flex items-center">
                                                <router-link :to="{ name: 'Edit', params: { id: data.id }}" class="inline-flex ml-2 items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="#1e40af" height="1em" viewBox="0 0 512 512"><path d="M362.7 19.3L314.3 67.7 444.3 197.7l48.4-48.4c25-25 25-65.5 0-90.5L453.3 19.3c-25-25-65.5-25-90.5 0zm-71 71L58.6 323.5c-10.4 10.4-18 23.3-22.2 37.4L1 481.2C-1.5 489.7 .8 498.8 7 505s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L421.7 220.3 291.7 90.3z"/></svg>
                                                    Edit
                                                </router-link>
                                            </div>
                                            <div class="flex items-center">
                                                <button @click="deleteData(data.id)" type="button" class="inline-flex ml-2 items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent text-blue-600 hover:text-blue-800 disabled:opacity-50 disabled:pointer-events-none dark:text-blue-500 dark:hover:text-blue-400 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="#1e40af" height="1em" viewBox="0 0 448 512"><path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/></svg>
                                                    Delete
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <div v-if="datalists.length == 0" class="min-w-full flex flex-col items-center">
                                <img 
                                    src="../assets/products_4x.gif"
                                    class="w-[40%]"
                                    alt="produk kosong">
                                <h2>Silahkan masukkan produk terlebih dahulu</h2>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
        </div>
    </div>
</template>