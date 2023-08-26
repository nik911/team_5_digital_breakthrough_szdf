<script lang="ts">
    export let description: string = "";
    export let advantages: string = "";
</script>

<section>
    <h2>3. Описание</h2>

    <label>Опишите стартап.</label>
    <textarea bind:value={description} />

    <label>
        Какие преимущества получат потребители при покупке вашего продукта или
        услуги?
    </label>
    <textarea bind:value={advantages} />
</section>
