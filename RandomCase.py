import sublime
import sublime_plugin

from random import randint

class RandomCaseCommand(sublime_plugin.TextCommand):
	def random_case(self, text):
		output = ""

		for c in text:
			swapped = c.upper() if randint(0,1) else c.lower()

			# Some characters change length when their case changes
			# (e.g. "ß".upper() == "SS"), so leave those alone
			output += swapped if len(swapped) == 1 else c

		return(output)

	def run(self, edit):
		for s in self.view.sel():
			region = s if s else self.view.word(s)
			text = self.view.substr(region)

			self.view.replace(edit, region, self.random_case(text))
