def option_schema(option) -> dict:
   return {
       "option": option
   }


def options_schema(options) -> list[dict]:
   return [option_schema(option) for option in options]


