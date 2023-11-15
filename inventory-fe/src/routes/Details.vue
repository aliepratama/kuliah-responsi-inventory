<script>
export default {
    props: ['id']
}
</script>
<template>
    <div>
        <div>
            <div class="max-w-4xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
                <!-- Card -->
                <div class="bg-white rounded-xl shadow p-4 sm:p-7 dark:bg-slate-900">
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
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Nama Produk
                            </span>
                        </div>
                    <!-- End Col -->

                        <div class="sm:col-span-9">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Nama Produk
                            </span>
                        </div>
                        <!-- End Col -->

                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Stok
                            </span>
                        </div>
                    <!-- End Col -->

                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Stok
                            </span>
                        </div>
                        <!-- End Col -->

                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Harga
                            </span>
                        </div>
                    <!-- End Col -->

                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Harga
                            </span>
                        </div>
                        <!-- End Col -->

                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Deskripsi
                            </span>
                        </div>
                    <!-- End Col -->
                        <div class="sm:col-span-9">
                            <textarea disabled id="textarea-label" class="py-2 px-3 pe-11 block w-full border-gray-200 shadow-sm text-sm rounded-lg focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600" rows="3"></textarea>
                        </div>
                        <!-- End Col -->
                        <div class="sm:col-span-3">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Kategori
                            </span>
                        </div>
                    <!-- End Col -->
                        <div class="sm:col-span-9">
                            <span class="inline-block text-sm font-medium text-gray-500 mt-2.5">
                                Kategori
                            </span>
                        </div>
                        <!-- End Col -->
                    </div>
                </div>
                <!-- End Card -->
                </div>
        </div>
    </div>
</template>