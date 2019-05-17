
import docx
import fileinput

class ReportTemplate():

	template_vars = {
		'<expert>': ''
	}

	template_file = None
	output_file = ''
	def __init__(self, template_file):
		self.template_file = template_file

	def set_expert_name(self, name):
		self.template_vars['<expert>'] = name
		self.output_file = name + '_' + hash(self)[5:] + '.docx'



	def write_template(self):
		with fileinput.input("test.txt", inplace=True) as fd:
			for line in fd:
				for k,v in self.template_vars.items():
					line.replace(k, v)
