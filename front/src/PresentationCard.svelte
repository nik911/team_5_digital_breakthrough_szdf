<script lang="ts">
    export let number: number;
    export let name: string;

    let ready = false;

    (async () => {
        await new Promise((r) => setTimeout(r, 10000));
        ready = true;
        // while (true) {
        //     try {
        //         let res = await fetch(`/${name}.pptx`);
        //         if (res.status === 200) {
        //             ready = true;
        //             break;
        //         } else {
        //             console.log(`${name} not ready yet`);
        //         }
        //     } catch (e) {
        //         console.log(e);
        //     }
        //     await new Promise((r) => setTimeout(r, 2000));
        // }
    })();
</script>

<article>
    <header>Вариант {number}</header>
    {#if ready}
        <a
            href={`${name}.pdf`}
            target="_blank"
            role="button"
            class="secondary"
            style="width:100%; margin-bottom: 1rem"
        >
            Предпросмотр
        </a>
        <a
            href={`${name}.pptx`}
            role="button"
            target="_blank"
            style="width:100%"
        >
            Скачать .pptx
        </a>
    {:else}
        <p aria-busy="true">Презентация в процессе, подождите...</p>
    {/if}
</article>
