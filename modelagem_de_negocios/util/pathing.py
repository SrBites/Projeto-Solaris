from flask import Flask
import os

class Path:
    def daWay(self):
        template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        template_dir = os.path.join(template_dir, 'modelagem_de_negocios')
        template_dir = os.path.join(template_dir, 'interface')
        template_dir = os.path.join(template_dir, 'templates')

        static_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        static_dir = os.path.join(static_dir, 'modelagem_de_negocios')
        static_dir = os.path.join(static_dir, 'interface')
        static_dir = os.path.join(static_dir, 'static')

        return Flask(__name__, template_folder=template_dir, static_folder=static_dir)