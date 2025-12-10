import { SfeirThemeInitializer } from '../web_modules/sfeir-school-theme/dist/sfeir-school-theme.mjs';

// One method per module
function schoolSlides() {
  return ['00-school/00-TITLE.md', '00-school/speaker-tanguy.md', '00-school/speaker-baptiste.md'];
}

function introSlides() {
  return ['intro/00-TITLE.md', 'intro/01-introduction-agents.md', 'intro/99-lab-workshop-example.md'];
}

function outillageSlides() {
  return [
    '01-outillage/00-TITLE.md',
    '01-outillage/01-introduction-tooling.md',
    '01-outillage/02-gemini-tools.md',
    '01-outillage/03-third-party-tools.md',
    '01-outillage/04-custom-tools.md',
    '01-outillage/05-best-practices.md'
  ];
}

function sessionMemoireSlides() {
  return ['02-session-memoire/00-TITLE.md'];
}

function multiAgentsSlides() {
  return [
    '03-multi-agents/00-TITLE.md',
    '03-multi-agents/01-intro.md',
    '03-multi-agents/02-sequential-agent.md',
    '03-multi-agents/03-parallel-agent.md',
    '03-multi-agents/04-loop-agent.md',
    '03-multi-agents/05-agent-tool.md',
    '03-multi-agents/06-custom-agent.md',
    '03-multi-agents/07-a2a-protocol.md',
  ];
}

function fonctionnalitesAvanceesSlides() {
  return ['04-fonctionnalites-avancees/00-TITLE.md'];
}

export function formation() {
  return [
    //
    ...schoolSlides(),
    ...introSlides(),
    ...outillageSlides(),
    ...sessionMemoireSlides(),
    ...multiAgentsSlides(),
    ...fonctionnalitesAvanceesSlides(),
  ].map((slidePath) => {
    return { path: slidePath };
  });
}

SfeirThemeInitializer.init(formation);
