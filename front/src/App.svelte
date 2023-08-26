<script>
  import Contacts from "./questions/Contacts.svelte";
  import Description from "./questions/Description.svelte";
  import Functionality from "./questions/Functionality.svelte";
  import Invests from "./questions/Invests.svelte";
  import Problem from "./questions/Problem.svelte";
  import Roadmap from "./questions/Roadmap.svelte";
  import Team from "./questions/Team.svelte";
  import Title from "./questions/Title.svelte";
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
    <Title />
    <Problem />
    <Description />
    <Functionality />
    <Team />
    <Invests />
    <Roadmap />
    <Contacts />

    <button
      on:click|preventDefault={() => alert("пока не)")}
      style="width: 100%; padding: 1.5rem"
    >
      Сгенерировать презентацию
    </button>
  </form>
</main>
