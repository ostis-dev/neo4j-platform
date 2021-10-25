## Development

- Run neo4j is a requirement to run code in development process. [Run official docker](https://neo4j.com/developer/docker/) is easiest way to do that.

- Create configuration file `config.ini`. See [config.ini](db/config.ini)

## Regenerate ANTLR parser

- [Download](https://www.antlr.org/download.html) antlr generator.
- Run generation script `./scripts/generate_antlr.sh antlr-4.9.2-complete.jar`