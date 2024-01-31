from django.db import models


class Team(models.Model):
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, description: {self.description}'


class Player(models.Model):
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, description: {self.description}'

class Injury(models.Model):
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, description: {self.description}'


