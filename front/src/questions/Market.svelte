<script lang="ts">
    export let industry = "";
    export let clientsAmount = "";
</script>

<section>
    <h2>5. Рынок</h2>

    <label>
        Какое направление деятельности у вашей копании? На каком рынке вы
        находитесь?
    </label>
    <input bind:value={industry} />

    <label>На какое количество клиентов вы ориентириуетсь?</label>
    <input bind:value={clientsAmount} />
</section>
