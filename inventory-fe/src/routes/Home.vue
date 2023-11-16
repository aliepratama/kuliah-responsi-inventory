<script>
</script>
<template>
    <div class="min-w-full mt-4 flex flex-col items-center">
        <img 
            src="../assets/home_4x.gif"
            class="w-[40%] hidden md:block"
            alt="inventory management">
        <div class="min-w-full px-36 mt-16 md:mt-0 flex flex-col items-center md:flex-row md:justify-between">
            <div class="flex flex-col items-center md:items-start">
                <h2 class="text-3xl font-extrabold text-center md:text-left">Inventory Management App</h2>
                <p class="mt-4 text-lg font-medium text-center md:text-left">Kelola produk anda di aplikasi ini</p>
            </div>
            <router-link to="/products" type="button" class="py-2 px-4 mt-16 md:mt-0 max-w-[5rem] text-center inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600">
                Mulai
            </router-link>
        </div>
    </div>
</template>