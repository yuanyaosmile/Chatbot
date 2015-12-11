# -*- coding: utf8 -*-
import aiml
import os
import config as cfg


class ChatBot(aiml.Kernel):
    def __init__(self, properties=cfg.BOT_PROPERTIES):
        aiml.Kernel.__init__(self)
        self.verbose(cfg.DEBUG)
        if os.path.isfile("billybot.brn"):
            self.bootstrap(brainFile="billybot.brn")
        else:
            self.init_bot()
            self.saveBrain("billybot.brn")
        for p in properties:
            self.setBotPredicate(p, properties[p])

    def init_bot(self):
        for file in os.listdir(cfg.AIML_SET):
            if file[-4::] == "aiml":
                self.learn(os.path.join(cfg.AIML_SET, file))


if __name__ == "__main__":
    bot = ChatBot()
    while True: print bot.respond(raw_input("( Barry)> "))
