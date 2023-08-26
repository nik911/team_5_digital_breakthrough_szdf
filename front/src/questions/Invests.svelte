<script lang="ts">
    export let investsAmount = "";
    export let investsTarget = "";
</script>

<section>
    <h2>6. Инвестиции</h2>

    <label>Каков необходимый объем инвестиций?</label>
    <input bind:value={investsAmount} />

    <label>Куда будут направлены полученные средства?</label>
    <textarea bind:value={investsTarget} />
</section>
