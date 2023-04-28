from kerykeion import (
    KerykeionSubject,
    NatalAspects,
)

from .expected_natal_aspects import EXPECTED_ALL_ASPECTS, EXPECTED_RELEVANT_ASPECTS

class TestNatalAspects:
    def setup_class(self):
        self.subject = KerykeionSubject("Johnny Depp", 1963, 6, 9, 0, 0, "Owensboro", "US")
        self.subject_relevant_aspects = NatalAspects(self.subject).get_relevant_aspects()
        self.subject_all_aspects = NatalAspects(self.subject).get_all_aspects()

        self.expected_relevant_aspects = EXPECTED_RELEVANT_ASPECTS
        self.expected_all_aspects = EXPECTED_ALL_ASPECTS
    def test_relevant_aspects_length(self):
        assert len(self.expected_relevant_aspects) == 19

    def test_relevant_aspects(self):
        for i, aspect in enumerate(self.expected_relevant_aspects):
            assert self.subject_relevant_aspects[i]["p1_name"] == aspect["p1_name"]
            assert round(self.subject_relevant_aspects[i]["p1_abs_pos"], 3) == round(aspect["p1_abs_pos"], 3)
            assert self.subject_relevant_aspects[i]["p2_name"] == aspect["p2_name"]
            assert round(self.subject_relevant_aspects[i]["p2_abs_pos"], 3) == round(aspect["p2_abs_pos"], 3)
            assert self.subject_relevant_aspects[i]["aspect"] == aspect["aspect"]
            assert round(self.subject_relevant_aspects[i]["aspect_degrees"], 3) == round(aspect["aspect_degrees"], 3)
            assert self.subject_relevant_aspects[i]["aspect_degrees"] == aspect["aspect_degrees"]
            assert self.subject_relevant_aspects[i]["color"] == aspect["color"]
            assert self.subject_relevant_aspects[i]["aid"] == aspect["aid"]
            assert round(self.subject_relevant_aspects[i]["diff"], 3) == round(aspect["diff"], 3)
            assert self.subject_relevant_aspects[i]["p1"] == aspect["p1"]
            assert self.subject_relevant_aspects[i]["p2"] == aspect["p2"]

    def test_all_aspects_length(self):
        assert len(self.expected_all_aspects) == 33

    def test_all_aspects(self):
        for i, aspect in enumerate(self.expected_all_aspects):
            assert self.subject_all_aspects[i]["p1_name"] == aspect["p1_name"]
            assert round(self.subject_all_aspects[i]["p1_abs_pos"], 3) == round(aspect["p1_abs_pos"], 3)
            assert self.subject_all_aspects[i]["p2_name"] == aspect["p2_name"]
            assert round(self.subject_all_aspects[i]["p2_abs_pos"], 3) == round(aspect["p2_abs_pos"], 3)
            assert self.subject_all_aspects[i]["aspect"] == aspect["aspect"]
            assert round(self.subject_all_aspects[i]["orbit"], 3) == round(aspect["orbit"], 3)
            assert round(self.subject_all_aspects[i]["aspect_degrees"], 3) == round(aspect["aspect_degrees"], 3)
            assert self.subject_all_aspects[i]["color"] == aspect["color"]
            assert self.subject_all_aspects[i]["aid"] == aspect["aid"]
            assert round(self.subject_all_aspects[i]["diff"], 3) == round(aspect["diff"], 3)
            assert self.subject_all_aspects[i]["p1"] == aspect["p1"]
            assert self.subject_all_aspects[i]["p2"] == aspect["p2"]