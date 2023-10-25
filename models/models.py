# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'

    nombre = fields.Char(required=True, help="Introducir nombre")
    descripcion = fields.Text()
    horas = fields.Integer()
    fecha_creacion = fields.Date()
    fecha_comienzo = fields.Datetime()
    fecha_fin = fields.Datetime()
    pausada = fields.Boolean()
    sprint = fields.Many2one("tareas.sprint")
    tecnologias = fields.Many2many("tareas.tecnologias")

class sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'tareas.sprint'

    nombre = fields.Char()
    descripcion = fields.Text()
    fecha_creacion = fields.Datetime()
    fecha_fin = fields.Datetime()
    tarea = fields.One2many("tareas.tareas", "sprint")

class tecnologias(models.Model):
    _name = 'tareas.tecnologias'
    _desription = 'tareas.tecnologias'

    nombre = fields.Char()
    imagen = fields.Image(maxwidth=200, maxheight=200)
