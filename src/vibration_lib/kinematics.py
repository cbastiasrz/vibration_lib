
import numpy as np
from dataclasses import dataclass


@dataclass(frozen=True)
class Bearing:
    """Geometría de un rodamiento de bolas.

    Parameters
    ----------
    n_balls : int
        Número de bolas.
    ball_d : float
        Diámetro de bola (mm).
    pitch_d : float
        Diámetro primitivo (mm).
    contact_angle : float
        Ángulo de contacto (grados).

    References
    ----------
    Randall, R. B., & Antoni, J. (2011). Rolling element bearing diagnostics—A tutorial. 
    *Mechanical Systems and Signal Processing*, *25*(2), 485–520. [https://doi.org/10.1016/j.ymssp.2010.07.017](https://doi.org/10.1016/j.ymssp.2010.07.017)

    Examples
    --------
    >>> b = Bearing(n_balls=9, ball_d=7.94, pitch_d=39.04, contact_angle=0)
    >>> round(b.bpfo(speed_hz=29.95), 2)
    107.36
    """

    n_balls: int
    ball_d: float
    pitch_d: float
    contact_angle: float

    def bpfo(self, speed_hz: float) -> float:
        """Calcula la frecuencia de paso de la bola exterior (BPFO).

        Parameters
        ----------
        speed_hz : float
            Frecuencia del eje (Hz).

        Returns
        -------
        float
            Frecuencia de paso de la bola exterior (Hz).
        """
        ratio = self.ball_d / self.pitch_d * np.cos(np.radians(self.contact_angle))

        return (
            self.n_balls * speed_hz / 2 * (1 - ratio)
        )

    def bpfi(self, speed_hz: float) -> float:
        """Calcula la frecuencia de paso de la bola interior (BPFI).

        Parameters
        ----------
        speed_hz : float
            Frecuencia del eje (Hz).

        Returns
        -------
        float
            Frecuencia de paso de la bola interior (Hz).
        """
        ratio = self.ball_d / self.pitch_d * np.cos(np.radians(self.contact_angle))
        return (
            self.n_balls * speed_hz / 2 * (1 + ratio)
        )

    def ftf(self, speed_hz: float) -> float:
        """Calcula la frecuencia de giro del anillo (FTF).

        Parameters
        ----------
        speed_hz : float
            Frecuencia del eje (Hz).

        Returns
        -------
        float
            Frecuencia de giro del anillo (Hz).
        """
        ratio = self.ball_d / self.pitch_d * np.cos(np.radians(self.contact_angle))
        return (
            speed_hz / 2 * (1 - ratio)
        )

    def bsf(self, speed_hz: float) -> float:
        """Calcula la frecuencia de paso de la bola (BSF).

        Parameters
        ----------
        speed_hz : float
            Frecuencia del eje (Hz).

        Returns
        -------
        float
            Frecuencia de paso de la bola (Hz).
        """
        ratio = self.ball_d / self.pitch_d * np.cos(np.radians(self.contact_angle))
        return (
            self.pitch_d / (2 * self.ball_d) * speed_hz * (1 - ratio ** 2)
        )