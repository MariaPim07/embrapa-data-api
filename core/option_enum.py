from enum import Enum

from fastapi import HTTPException


class Option(Enum):
    OPTION_1 = "subopt_01"
    OPTION_2 = "subopt_02"
    OPTION_3 = "subopt_03"
    OPTION_4 = "subopt_04"
    OPTION_5 = "subopt_05"

    def get_option(self, option):
        process = {"viniferas": self.OPTION_1.value,
                   "americanas": self.OPTION_2.value,
                   "hibridas": self.OPTION_3.value,
                   "uvas_de_mesa": self.OPTION_4.value,
                   "sem_classificacao": self.OPTION_5.value,
                   "vinhos_de_mesa": self.OPTION_1.value,
                   "espumantes": self.OPTION_2.value,
                   "uvas_frescas": self.OPTION_3.value,
                   "uvas_passa": self.OPTION_4.value,
                   "suco_de_uva": self.OPTION_5.value}

        if option not in process.keys(): raise HTTPException(400, "invalid option.")

        return process[option]