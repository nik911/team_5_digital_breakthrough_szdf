<script lang="ts">
  import PresentationCard from "./PresentationCard.svelte";
  import Competitors from "./questions/Competitors.svelte";
  import Contacts from "./questions/Contacts.svelte";
  import Description from "./questions/Description.svelte";
  import Functionality from "./questions/Functionality.svelte";
  import Invests from "./questions/Invests.svelte";
  import Market from "./questions/Market.svelte";
  import Problem from "./questions/Problem.svelte";
  import Roadmap from "./questions/Roadmap.svelte";
  import Team from "./questions/Team.svelte";
  import Title from "./questions/Title.svelte";

  let data: any = {};

  let state = 0;

  async function onDataGenerate() {
    console.log(JSON.stringify(data));
    state = 1;
    await new Promise((r) => setTimeout(r, 2000));
    state = 2;
  }
</script>

<header>
  <hgroup>
    <h2>Pitchdecker</h2>
    <p>
      Питч-дек — это просто! Резюмируйте свой стартап, ответив на несколько
      вопросов, а искусственный интеллект сделает для вас информативную и
      красивую презентацию.
    </p>
  </hgroup>
</header>
<hr />
<main>
  <form>
    <Title bind:title={data.title} />
    <Problem bind:problem={data.problem} bind:target={data.target} />
    <Description
      bind:description={data.description}
      bind:advantages={data.advantages}
    />
    <Functionality bind:functionality={data.functionality} />
    <Market
      bind:industry={data.industry}
      bind:clientsAmount={data.clientsAmount}
    />
    <Competitors bind:inn={data.inn} />
    <Team bind:team={data.team} />
    <Invests
      bind:investsAmount={data.investsAmount}
      bind:investsTarget={data.investsTarget}
    />
    <Roadmap bind:roadmap={data.roadmap} />
    <Contacts
      bind:email={data.email}
      bind:phone={data.phone}
      bind:address={data.address}
    />

    <section>
      <button
        on:click|preventDefault={onDataGenerate}
        style="width: 100%; padding: 1.5rem"
        disabled={state === 1}
        aria-busy={state === 1}
      >
        Сгенерировать презентацию
      </button>
    </section>
  </form>
  {#if state === 2}
    <p>Выберите предпочтительный стиль презентации:</p>
    <div class="grid">
      <PresentationCard number={1} name="pattern1" />
      <PresentationCard number={2} name="pattern2" />
      <PresentationCard number={3} name="pattern3" />
    </div>
  {/if}
</main>
