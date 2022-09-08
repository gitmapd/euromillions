import rich


class MyConfirm(prompt.Confirm):
    validate_error_message = "[prompt.invalid]Por favor introduzir S ou N"
    choices=['s','n']

class MyPrompt(prompt.PromptBase):
    validate_error_message = "[prompt.invalid]Por favor entra um valor válido"
    illegal_choice_message = (
        "[prompt.invalid.choice]Por favor seleciona uma das opções disponíveis"
    )
    prompt_suffix = ": "
