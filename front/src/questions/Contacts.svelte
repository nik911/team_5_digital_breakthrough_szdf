<script lang="ts">
    export let email = "";
    export let phone = "";
    export let address = "";
</script>

<section>
    <h2>10. Контактная информация</h2>

    <label>Укажите номер телефона</label>
    <input type="tel" bind:value={phone} />
    <label>Укажите адрес электронной почты</label>
    <input type="email" bind:value={email} />
    <label>Укажите физический адрес вашей компании</label>
    <input bind:value={address} />
</section>
