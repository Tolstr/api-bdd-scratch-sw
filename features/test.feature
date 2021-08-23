Feture: SWAPI people
    Scenario Outline: Verify people
        When I am making request I am getting right name, birth_year, url, status_code
        Examples:
        |name           |birth_year |url        |status_code |
        |Luke Skywalker |19BBY      |people/1/  |200         |

