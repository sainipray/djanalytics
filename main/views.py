# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from main.stackoverflow import get_latest_questions, get_popular_tags, get_top_users, get_top_users_of_tag
from main.twitterapi import TwitterApi, tweets_analysis


class TwitterAnalyticsDashboard(TemplateView):
    template_name = 'twitter.html'

    def get_context_data(self, **kwargs):
        tt = TwitterApi()
        context = super(TwitterAnalyticsDashboard, self).get_context_data(**kwargs)
        context['username'] = kwargs.get('username', None)
        if context['username']:
            try:
                context['tweets'] = tt.get_user_tweets(context['username'], number_of_tweets=200)
                context['profile'] = tt.get_user_profile(context['username'])
                context['analysis'] = tweets_analysis(context['tweets'])
            except Exception as e:
                from django.http import Http404
                raise Http404(e.response.reason)
        return context


class Stackoverflow(TemplateView):
    template_name = 'stackoverflow.html'

    def get_context_data(self, **kwargs):
        context = super(Stackoverflow, self).get_context_data(**kwargs)
        type = self.request.GET.get('type', None)
        data = None
        if type == "questions":
            data = get_latest_questions()
        elif type == "tags":
            data = get_popular_tags()
        elif type == "users":
            data = get_top_users()
        elif type == "tag_users":
            tagname = self.request.GET.get('tagname', None)
            if tagname:
                data = get_top_users_of_tag(tagname)
        if data:
            context['data'] = data['data']
            context['keys'] = data['keys']
        return context
