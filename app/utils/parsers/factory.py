from typing import Dict

from utils.const import Constansts
from utils.parsers import WebParser
from utils.parsers.meta_critic_web_parser import MetaCriticWebParser


WebParserFactory: Dict[str, WebParser] = {
    Constansts.METACRITIC_APP_URL: MetaCriticWebParser()
}
