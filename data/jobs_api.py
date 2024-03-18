import flask

from . import db_session
from .jobs import Jobs
from flask import request

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/api/jobs/<job_id>', methods=['GET'])
def get_jobs_2(job_id):
    db_sess = db_session.create_session()

    try:
        job = db_sess.query(Jobs).get(job_id)

        if not job:
            return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)

        data = {
            'jobs': [{'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'collaborators': job.collaborators,
                      'is_finished': job.is_finished, 'start_date': job.start_date, 'end_date': job.end_date}]}
        return flask.jsonify(data)

    except Exception:
        pass


@blueprint.route('/api/jobs', methods=['GET', 'POST'])
def get_jobs_3():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        jobs = db_sess.query(Jobs).all()
        data = {'jobs': [{'id': job.id, 'team_leader': job.team_leader, 'job': job.job, 'collaborators': job.collaborators,
                          'is_finished': job.is_finished, 'start_date': job.start_date, 'end_date': job.end_date} for job in
                         jobs]}
        return flask.jsonify(data)
    elif request.method == 'POST':
        if not request.json:
            return flask.make_response(flask.jsonify({'error': 'Empty request'}), 400)
        elif not all(key in request.json for key in
                     ['team_leader', 'work_size', 'collaborators', 'is_finished', 'job']):
            return flask.make_response(flask.jsonify({'error': 'Bad request'}), 400)
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=request.json['team_leader'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            job=request.json['job'],
            is_finished=request.json['is_finished']
        )
        db_sess.add(job)
        db_sess.commit()
        return jsonify({'id': job.id})
