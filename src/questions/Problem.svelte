<script lang="ts">
    export let problem: string = "";
    export let target: string = "";
</script>

<section>
    <h2>2. Проблематкиа</h2>

    <label for="textarea">Какая проблема вашего проекта?</label>
    <textarea bind:value={problem} />

    <label for="textarea">Какова целевая аудитория проекта?</label>
    <textarea bind:value={target} />
</section>
