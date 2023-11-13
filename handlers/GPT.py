from aiogram import Router, types
import openai
from aiogram.filters.command import Command, CommandObject


openai.api_key = 'YOUR_GPT_TOKEN'

router = Router()

@router.message(Command("gpt"))
async def GPT(
    message: types.Message,
    command: CommandObject
):
    # Функия 
    usr_text = command.args
    usr_msg = []
    usr_msg.append({'role': 'user', 'content': usr_text})
    chat = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = usr_msg
    )
          
    reply = chat.choices[0].message.content
    usr_msg.append({'role': 'assistant', 'content': reply})

    await message.reply(reply)

