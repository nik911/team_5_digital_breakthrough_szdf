<script lang="ts">
    export let title: string = "";
</script>

<section>
    <h2>1. Название проекта</h2>

    <label>Как называется ваш проект?</label>
    <input bind:value={title} />
</section>
