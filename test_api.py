from unittest.mock import Mock, patch
from api import quit_rate_api
import json

def test_quit_rate_api():
    fake_response = Mock()
    fake_response.text = json.dumps( {"Results": {
                                            "series": [
                                            {
                                            "seriesID": "JTS000000000000000JOR",
                                            "data": [
                                            {
                                                "year": "2026",
                                                "period": "M02",
                                                "periodName": "February",
                                                "latest": "true",
                                                "value": "4.2",
                                            "footnotes": [
                                            {
                                                "code": "P",
                                                "text": "preliminary"
                                            }]}]}]}})

    with patch("api.requests.post", return_value = fake_response):
        results = quit_rate_api()
        assert type(results) == list
        assert results[0]["year"] == "2026"
        assert results[0]["period"] == "M02"
        assert results[0]["value"] == "4.2"
        assert "year" in results[0]

def test_missing_key():
    fake_response = Mock()
    fake_response.text = json.dumps( {"wrong word": {
                                            "bad error": [
                                            {
                                            "seriesID": "JTS000000000000000JOR",
                                            "data": [
                                            {
                                                "year": "2026",
                                                "period": "M02",
                                                "periodName": "February",
                                                "latest": "true",
                                                "value": "4.2",
                                            "footnotes": [
                                            {
                                                "code": "P",
                                                "text": "preliminary"
                                            }]}]}]}})
    with patch("api.requests.post", return_value = fake_response):
        assert quit_rate_api() == "Missing or incorrect results in response"
    
def test_wrong_id():
    fake_response = Mock()
    fake_response.text = json.dumps( {"Results": {
                                            "series": [
                                            {
                                            "seriesID": "12345",
                                            "data": [
                                            ]}]}})
    with patch("api.requests.post", return_value = fake_response):
        assert quit_rate_api() == []

def test_api_limit():
    fake_response = Mock()
    fake_response.text = json.dumps({"message": ['Request could not be serviced, as the daily threshold for total number of requests allocated to the user with registration key has been reached.']})
    with patch("api.requests.post", return_value = fake_response):
        results = quit_rate_api()
        assert {'year': '2025', 'period': 'M10', 'value': '4.3'} in results

def test_missing_value():
    fake_response = Mock()
    fake_response.text = json.dumps( {"Results": {
                                            "series": [
                                            {
                                            "seriesID": "JTS000000000000000JOR",
                                            "data": [
                                            {
                                                "year": "2026",
                                                "period": "M02",
                                                "periodName": "February",
                                                "latest": "true",
                                                "value": "4.2",
                                            "footnotes": [
                                            {
                                                "code": "P",
                                                "text": "preliminary"
                                            }]}]}]}})

    with patch("api.requests.post", return_value = fake_response):
        assert quit_rate_api() == "Missing or incorrect results in response"



def test_missing_value():
    fake_response = Mock()
    fake_response.text = json.dumps( {"Results": {
                                            "series": [
                                            {
                                            "seriesID": "JTS000000000000000JOR",
                                            "data": [
                                            {
                                                }]}]}})

    with patch("api.requests.post", return_value = fake_response):
        assert quit_rate_api() == "Missing or incorrect results in response"


def test_wrong_type():
    fake_response = Mock()
    fake_response.text = json.dumps( {"Results": {
                                            "series": [
                                            {
                                            "seriesID": "JTS000000000000000JOR",
                                            "data": [
                                            {
                                                "year": ["2026", "two things"],
                                                "period": "M02",
                                                "periodName": "February",
                                                "latest": "true",
                                            "footnotes": [
                                            {
                                                "code": "P",
                                                "text": "preliminary"
                                            }]}]}]}})

    with patch("api.requests.post", return_value = fake_response):
        assert quit_rate_api() == "Missing or incorrect results in response"