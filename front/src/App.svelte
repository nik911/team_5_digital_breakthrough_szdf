<script lang="ts">
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

  async function onDataGenerate() {
    console.log(JSON.stringify(data));
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
    <Market bind:industry={data.industry} />
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

    <button
      on:click|preventDefault={onDataGenerate}
      style="width: 100%; padding: 1.5rem"
    >
      Сгенерировать презентацию
    </button>
  </form>
</main>
