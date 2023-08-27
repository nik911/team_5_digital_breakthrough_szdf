<script lang="ts">
    export let team = [{ fullName: "", role: "" }];

    export let investors: string[] = [];

    function onAddInvestors() {
        investors.push("");
        investors = investors;
    }

    function onRemoveInvestors() {
        investors.pop();
        investors = investors;
    }

    function onAddTeamEntry() {
        team.push({ fullName: "", role: "" });
        team = team;
    }

    function onRemoveTeamEntry() {
        team.pop();
        team = team;
    }
</script>

<section>
    <h2>7. Команда</h2>

    <label>Заполните информацию о членах команды стартапа.</label>
    {#each team as entry}
        <form role="group">
            <input bind:value={entry.fullName} placeholder="ФИО" />
            <input bind:value={entry.role} placeholder="Роль" />
        </form>
    {/each}

    <button
        style="margin-bottom: 2rem"
        class="secondary"
        on:click|preventDefault={onAddTeamEntry}
    >
        Добавить
    </button>

    {#if team.length > 1}
        <button
            class="outline secondary"
            on:click|preventDefault={onRemoveTeamEntry}
        >
            Убрать
        </button>
    {/if}

    <label>Заполните информацию о текущих инвесторах (если есть).</label>
    {#each investors as entry}
        <input bind:value={entry} placeholder="ФИО" />
    {/each}

    <button class="secondary" on:click|preventDefault={onAddInvestors}>
        Добавить
    </button>

    {#if investors.length > 0}
        <button
            class="outline secondary"
            on:click|preventDefault={onRemoveInvestors}
        >
            Убрать
        </button>
    {/if}
</section>
