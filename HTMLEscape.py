import sublime
import sublime_plugin
import html
from html.parser import HTMLParser

class HTMLEntityCommand(sublime_plugin.TextCommand):
  def form_selection(self, region):
    # if nothing's selected, escape the whole file
    if region.empty():
      return sublime.Region(0, self.view.size())

    return region

  def process(self, text):
    return ""

  def run(self, edit):
    for region in self.view.sel():
      selection = self.form_selection(region)
      selected_text = self.view.substr(selection)
      self.view.replace(edit, selection, self.process(selected_text))

class EscapehtmlCommand(HTMLEntityCommand):
  """Escapes HTML entities."""
  def process(self, text):
    escaped = html.escape(text)
    escaped = escaped.replace("&#x27;", "&apos;") # fix for '
    return escaped

class UnescapehtmlCommand(HTMLEntityCommand):
  """Unescapes HTML entities."""
  def process(self, text):
    return HTMLParser().unescape(text)

