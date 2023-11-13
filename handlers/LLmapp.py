from llama_index import SimpleDirectoryReader, ServiceContext, GPTVectorStoreIndex
from llama_index.llms import OpenAI
from aiogram import Router, types
import openai
from aiogram.filters.command import Command, CommandObject



openai.api_key = 'YOUR_GPT_TOKEN' #Api
router = Router()

@router.message(Command("llma"))
async def LLma(
    message: types.Message,
    command: CommandObject
):
    llm = OpenAI(temperature=0, model='gpt-3.5-turbo')# Задается темература и версия GPT
    service_context = ServiceContext.from_defaults(llm=llm)
    usr_text = command.args # Задает в переменую текст ввода после команда в ТГ
    documents = SimpleDirectoryReader('handlers/data').load_data() # Считывет файл с папки
    index = GPTVectorStoreIndex.from_documents(
	documents,
	service_context=service_context
) #
    query_engine = index.as_query_engine()
    response = query_engine.query(usr_text) # генерация ответа
    await message.reply(str(response)) # Выврд ответа

