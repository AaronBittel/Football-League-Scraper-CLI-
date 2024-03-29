from __future__ import annotations

import copy
from dataclasses import dataclass, field

from bundesliga_scraper.datatypes.matchday import Matchday
from bundesliga_scraper.datatypes.table_entry import TableEntry


@dataclass
class Table:
    league_name: str
    teams: dict[str, TableEntry] = field(default_factory=dict)
    standings: list[TableEntry] = field(default_factory=list)

    def calculate_table(
        self, matchdays: list[Matchday], home: bool = True, away: bool = True
    ) -> None:
        for matchday in matchdays:
            for fixture in matchday.fixtures:
                if not fixture.match_is_finished and not fixture.match_is_live:
                    continue
                if home:
                    self.teams[fixture.home_team].update(fixture)
                if away:
                    self.teams[fixture.away_team].update(fixture)

            self._update_teams_history()

        self.matchday = max(team.matches for team in self.teams.values())

    def _update_teams_history(self):
        self._sort()
        for pl, table_entry in enumerate(self.standings, start=1):
            self.teams[table_entry.team_name].history.placements.append(pl)
            self.teams[table_entry.team_name].history.points.append(table_entry.points)

    def _sort(self) -> None:
        self.standings = sorted(self.teams.values(), reverse=True)

    def copy(self) -> Table:
        return copy.deepcopy(self)
