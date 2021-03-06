import sublime
import sublime_plugin

from random import randint

class RandomCase(sublime_plugin.TextCommand):
	def random_case(self, text):
		output = ""

		for c in text.upper():
			if randint(0,1):
				output += c.lower()
			else:
				output += c

		return(output)

	def run(self, edit):
		for s in self.view.sel():
			region = s if s else view.word(s)
			text = self.view.substr(region)
			
			# Preserve leading and trailing whitespace
			leading = text[:len(text)-len(text.lstrip())]
			trailing = text[len(text.rstrip()):]

			newtext = leading + self.random_case(text) + trailing

			self.view.replace(edit, region, newtext)