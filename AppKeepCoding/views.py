from django.http import HttpResponse
from django.shortcuts import render
from AppKeepCoding.models import Curso, Estudiante, Profesor, Entregable
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre='SQL', camada="1000")
    curso.save()
    documentoDeTexto = {f"Curso: {curso.nombre}, camada: {curso.camada}"}
    return HttpResponse(documentoDeTexto)

def estudiante(self):
    estudiante = Estudiante(nombre='Losif', apellido="Mondoc", email='losif@telefonica.com')
    estudiante.save()
    documentoDeTexto = {f"Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}, Email: {estudiante.email}"}
    return HttpResponse(documentoDeTexto)

def profesor(self):
    profesor = Profesor(nombre='Pepe', apellido="Garcia", email='pepe@gmail.com', profesion='Profesor')
    profesor.save()
    documentoDeTexto = {f"Nombre: {profesor.nombre}, Apellido: {profesor.apellido}, Email: {profesor.email}, Profesion: {profesor.profesion}"}
    return HttpResponse(documentoDeTexto)

def entregable(self):
    entregable = Entregable(nombre='tarea1', fechaDeEntrega="2022-05-01", entregado=True)
    entregable.save()
    documentoDeTexto = {f"Nombre: {entregable.nombre}, Fecha de entrega: {entregable.fechaDeEntrega}, Entregado: {entregable.entregado}"}
    return HttpResponse(documentoDeTexto)