<script lang="ts">
    export let email = "";
    export let phone = "";
    export let website = "";
</script>

<section>
    <h2>8. Контактная информация</h2>

    <label>Укажите номер телефона</label>
    <input type="tel" bind:value={phone} />
    <label>Укажите адрес электронной почты</label>
    <input type="email" bind:value={email} />
    <label>Укажите ссылку на вебсайт проекта (необязательно)</label>
    <input type="url" bind:value={website} />
</section>
