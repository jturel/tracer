from . import View
from tracer.resources.lang import _
from tracer.views.note_for_hidden import NoteForHiddenView


class DefaultView(View):
	def render(self):

		with_helpers = self.args.applications.with_helpers()
		without_helpers = self.args.applications.without_helpers()
		note = self.args.session_count or self.args.static_count

		if with_helpers or without_helpers:
			print _("you_should_restart")

		if len(with_helpers):
			print "  " + _("restart_using_helpers")
			for application in with_helpers.sorted("helper"):
				print "      " + application.helper

			if without_helpers:
				print ""

		if len(without_helpers):
			print "  " + _("restart_manually")
			for application in without_helpers.sorted("name"):
				print "      " + application.name

			if note:
				print ""

		if with_helpers and not without_helpers and note:
			print ""

		if not self.args.args.all:
			view = NoteForHiddenView()
			view.assign("args", self.args.args)
			view.assign("total_count", self.args.total_count)
			view.assign("session_count", self.args.session_count)
			view.assign("static_count", self.args.static_count)
			view.render()
