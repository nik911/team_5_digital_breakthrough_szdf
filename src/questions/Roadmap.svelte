<script lang="ts">
    export let roadmap = [{ date: null, goal: "" }];

    function onAddRoadmap() {
        roadmap.push({ date: null, goal: "" });
        roadmap = roadmap;
    }

    function onRemoveRoadmap() {
        roadmap.pop();
        roadmap = roadmap;
    }
</script>

<section>
    <h2>7. Дорожная карта</h2>

    <label>Заполните информацию о дорожной карте проекта.</label>
    {#each roadmap as entry}
        <form role="group">
            <input type="date" bind:value={entry.date} />
            <input bind:value={entry.goal} placeholder="Цель" />
        </form>
    {/each}

    <button
        style="margin-bottom: 2rem"
        class="secondary"
        on:click|preventDefault={onAddRoadmap}
    >
        Добавить
    </button>

    {#if roadmap.length > 1}
        <button
            class="outline secondary"
            on:click|preventDefault={onRemoveRoadmap}
        >
            Убрать
        </button>
    {/if}
</section>
