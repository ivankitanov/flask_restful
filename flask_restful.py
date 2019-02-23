from flask import Flask, request, jsonify 
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


students = ['Jack','Geralt','Steven','Pesho','Tony']
courses = ['Python', 'Maths' , 'English']
events = ['Board meeting', 'Voleyball tournament', 'Football tournament']

class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Name',
                        type=string,
                        required=True,
                        )

    def get(self, name):
        for student in students:
            if student['name'] == name:
                return student


class Course(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Name',
                        type=string,
                        required=True,
                        )

    def get(self, name):
        for course in courses:
            if course['name'] == name:
                return course


class Event(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Name',
                        type=string,
                        required=True,
                        )

    def get(self, name):
        for event in events:
            if event['name'] == name:
                return event


class StudentList(Resource):
    def get(self):
        return {'students': students}


api.add_resource(Student, '/student/<string:name>')
api.add_resource(StudentList, '/students')

class CourseList(Resource):
    def get(self):
        return {'courses': courses}


api.add_resource(Course, '/course/<string:name>')
api.add_resource(CourseList, '/courses')

class EventLIst(Resource):
    def get(self):
        return {'events': events}


api.add_resource(Event, '/event/<string:name>')
api.add_resource(EventLIst, '/events')
            
        


        
