<script lang="ts">
    export let roadmap = [{ date: "", goal: "" }];

    function onAddRoadmap() {
        roadmap.push({ date: "", goal: "" });
        roadmap = roadmap;
    }

    function onRemoveRoadmap() {
        roadmap.pop();
        roadmap = roadmap;
    }
</script>

<section>
    <h2>9. Дорожная карта</h2>

    <label>Заполните информацию о дорожной карте проекта.</label>
    {#each roadmap as entry}
        <form role="group">
            <input bind:value={entry.date} placeholder="Дата" />
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
